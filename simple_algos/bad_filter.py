import argparse
import json
import logging
import os
import sys

from apps import load_schema, API_BASE_PATH
from common.utils import filter_dict_keys as old_filter_dict_keys, shift_dict, get_project_root_dir, \
    set_utf8_as_default_encoding
from ss.customjsonschema import validate_schemas, resolve_schemas

log = logging.getLogger(__name__)

API_URI_PATH = '/metadata/v4.0'
ABS_BASE_PATH = os.path.join(get_project_root_dir(), API_BASE_PATH)
API_URI_PATH_EXCLUDE_LIST = (
    '/metadata/v4.0/.*', '/data/v4.0/.*', '/data/v4.0/organizations/{organization_id}/blobs/{sha256}',
    '/data/v4.0/organizations/{organization_id}/upload/{upload_id}'
)
STANDART_HEADERS = 'standard_headers'
ERROR_HEADERS = 'error_headers'
HEADERS_IGNORE_LIST = ('Access-Control-Expose-Headers',)
SWAGGER_ALLOW_TYPE = ('string', 'number', 'integer', 'boolean', 'array', 'file', 'object')
SWAGGER_ALLOW_FORMATS = ('int32', 'int64', 'long', 'float', 'double', 'binary', 'byte', 'date', 'date-time', 'password')
REQUEST_PARAMS_GROUPS = (
    {'name': 'uri_params_scheme', 'in': 'path'}, {'name': 'query_params_scheme', 'in': 'query'},
    {'name': 'headers_params_scheme', 'in': 'header'}
)


def parse_args():
    parser = argparse.ArgumentParser(description='SecuriSync api documentation generator')

    parser.add_argument('-p', '--path', metavar='PATH', type=str, default=ABS_BASE_PATH,
                        help='path to save document [%(default)s]')
    parser.add_argument('-n', '--name', metavar='NAME', type=str, default='API_SHEMA',
                        help='document name [%(default)s]')
    parser.add_argument('-f', '--format', metavar='FORMAT', type=str, choices=('json', 'yaml'), default='json',
                        help='format to save document [%(default)s]')
    parser.add_argument('-wp', '--without_params', action='store_true',
                        help='remove request params')
    parser.add_argument('-wb', '--without_body', action='store_true',
                        help='remove response body schema')
    parser.add_argument('-wh', '--without_headers', action='store_true',
                        help='remove response headers')
    parser.add_argument('-v', '--validate', action='store_true',
                        help='validate swagger file with python libraries')

    parser.add_argument('--with_oneOf', action='store_true',
                        help='add oneOf to json schema')

    args = parser.parse_args()

    return args


def filter_dict_keys(obj, func):
    if isinstance(obj, dict):
        obj = dict([item for item in obj.items() if func(item[1])])
        for k in obj:
            obj[k] = filter_dict_keys(obj[k], func)
    elif isinstance(obj, list):
        obj = [elem for elem in obj if func(elem)]
        for i, _ in enumerate(obj):
            obj[i] = filter_dict_keys(obj[i], func)
    elif isinstance(obj, tuple):
        obj = [elem for elem in obj if func(elem)]
        for i, _ in enumerate(obj):
            obj[i] = filter_dict_keys(obj[i], func)
    return obj


def merge_two_dict(a, b):
    for key in a.keys() + b.keys():
        if isinstance(a.get(key), dict) and isinstance(b, dict) and isinstance(b.get(key), dict):
            a[key] = merge_two_dict(a[key], b[key])
        elif isinstance(a.get(key), list) and isinstance(b, dict) and isinstance(b.get(key), list):
            try:
                result = list(set(a[key] + b[key]))
            except TypeError:
                result = a[key]
            a[key] = result
        elif isinstance(a.get(key), tuple) and isinstance(b, dict) and isinstance(b.get(key), tuple):
            try:
                result = list(set(list(a[key]) + list(b[key])))
            except TypeError:
                result = a[key]
            a[key] = result
        elif a.get(key) is None:
            a[key] = b.get(key)
    return a


def merge_additional_properties_to_obj(obj):
    additional_properties = obj.get('additionalProperties')
    if isinstance(additional_properties, dict):
        obj = merge_two_dict(obj, additional_properties)
        obj['additionalProperties'] = False
    return obj


def main():
    set_utf8_as_default_encoding()
    args = parse_args()

    SCHEMAS, URIS, URI_PATTERNS = load_schema()

    for URI in URIS:
        URIS[URI].pop('uri_re_pattern')

    URIS = resolve_schemas(URIS, SCHEMAS)
    validate_schemas(URIS)

    data = {
        'swagger': '2.0',
        'info': {
            'title': 'Metadata_v4',
            'description': 'Simple API for demonstrating json validation',
            'version': '4.0'
        },
        'host': 'sync.mod.net',
        'schemes': [
            'https'
        ],
        'basePath': API_URI_PATH,
        'consumes': [
            'application/json'
        ],
        'produces': [
            'application/json'
        ]
    }

    data['paths'] = URIS

    for path in data['paths']:
        path_info = data['paths'][path]
        if isinstance(path_info, dict):
            path_info.pop('resource_name', '')
            path_info.pop('path', '')
            methods = path_info.pop('methods', [])
            for method in methods:
                methods[method]['parameters'] = []
                if methods[method].get('info'):
                    info = methods[method].pop('info', {})
                    methods[method]['description'] = info.get('description', '')
                    methods[method]['operationId'] = info.get('operationId', '')
                    methods[method]['tags'] = info.get('tags', [])
                if methods[method].get('request'):
                    request = methods[method].pop('request', {})
                    if isinstance(request, dict):
                        if not args.without_params:
                            for request_params_group in REQUEST_PARAMS_GROUPS:
                                if request.get(request_params_group['name'], {}):
                                    request_params_group_scheme = request.get(request_params_group['name'])
                                    request_params_group_list = request_params_group_scheme.get(
                                        'oneOf') or request_params_group_scheme.get('allOf') or [
                                                                    request_params_group_scheme]
                                    for request_params in request_params_group_list:
                                        if request_params.get('properties', {}):
                                            params = request_params.get('properties', {})
                                            for param in params:
                                                key = params[param]
                                                key['name'] = param
                                                key['type'] = key.get('type') or 'string'
                                                key['in'] = request_params_group['in']
                                                key['required'] = key.get('required', False) or bool(
                                                    key['name'] in request_params.get('required', []))
                                                methods[method]['parameters'].append(key)
                        if not args.without_params:
                            if request.get('body', {}):
                                request_body = {
                                    'name': 'request_body',
                                    'in': 'body',
                                    'required': True,
                                    'schema': request['body'].get('scheme')
                                }
                                if request_body['schema']:
                                    methods[method]['parameters'].append(request_body)

                if methods[method].get('response'):
                    response = methods[method].pop('response', {})
                    responses = {
                        '200': {
                            'description': 'Good response',
                            'schema': {},
                            'headers': {}
                        },
                        'default': {
                            'description': 'Bad response',
                            'headers': {}
                        }
                    }
                    if not args.without_headers:
                        if response.get('headers_params_scheme', {}):
                            headers_params_scheme = response['headers_params_scheme']
                            headers_params_scheme_list = headers_params_scheme.get(
                                'oneOf') or headers_params_scheme.get('allOf') or [headers_params_scheme]
                            for headers_params_scheme in headers_params_scheme_list:
                                if headers_params_scheme.get('description', {}):
                                    if headers_params_scheme['description'] == STANDART_HEADERS:  # TODO: bad hardcoding
                                        good_headers = headers_params_scheme.get('properties')
                                        good_headers = {item[0]: item[1] for item in good_headers.items() if
                                                        item[0] not in HEADERS_IGNORE_LIST}
                                        responses['200']['headers'] = good_headers
                                    if headers_params_scheme['description'] == ERROR_HEADERS:  # TODO: bad hardcoding
                                        bad_headers = headers_params_scheme.get('properties')
                                        responses['default']['headers'] = bad_headers

                    response_schema = response.get('body', {}).get('scheme', {}) if not args.without_body else {}
                    responses['200']['schema'] = response_schema

                    methods[method]['responses'] = responses
                path_info[method] = methods[method]

    data['paths'] = {item[0]: item[1] for item in data['paths'].items() if item[0] not in API_URI_PATH_EXCLUDE_LIST}
    data['paths'] = {item[0].replace(API_URI_PATH, ''): item[1] for item in data['paths'].items()}
    data = filter_dict_keys(
        data, lambda value: True if value not in (None, unicode('null'))
        else False
    )  # TODO: fixpath_info it in metatada
    data = old_filter_dict_keys(data,
        lambda key, value: False if key == 'format' and value not in SWAGGER_ALLOW_FORMATS
        else True
    )  # TODO: fixpath_info it in metatada
    data = old_filter_dict_keys(data, lambda key, value: value)  # TODO: fipath_info it in metatada
    # data = old_filter_dict_keys(data, lambda key, value: False if key=='type' and value not in SWAGGER_ALLOW_TYPE else True)  #TODO: fixpath_info it in metatada
    data = shift_dict(
        data,
        dict_func=lambda obj:
            dict(map(
                lambda item: (item[0], item[1][0])
                    if bool(isinstance(item[1], (tuple, list)) and item[0] == 'type' and len(item[1]) == 1)
                    else item, obj.items()))
        if obj.get('type')
        else obj
    )  # TODO: change array to string in 'type' if one type
    data = shift_dict(data, dict_func=merge_additional_properties_to_obj)
    data = shift_dict(
        data,
        dict_func=lambda obj: dict(obj.items() + [('type', 'string'), ]) if obj.get('enum') and not obj.get('type')
        else obj
    )
    if not args.with_oneOf:
        data = shift_dict(
            data,
            dict_func=lambda obj: obj.get('oneOf')[0] if isinstance(obj.get('oneOf')(list, tuple))
            else obj
        )

    if args.format == 'yaml':
        file_yaml_name = os.path.join(args.path, '%s.yaml' % args.name)
        try:
            import yaml
            with open(file_yaml_name, 'w+') as yaml_shemas_file:
                yaml.safe_dump(data, yaml_shemas_file)
        except ImportError as err:
            sys.stdout.write(str(err))
            log.warning(err)

    if args.format == 'json':
        file_json_name = os.path.join(args.path, '%s.json' % args.name)
        with open(file_json_name, 'w+') as json_shemas_file:
            json.dump(data, json_shemas_file, indent=4)

    if args.validate:
        try:
            import flex
            if args.format == 'yaml':
                schema = flex.load(file_yaml_name)
            elif args.format == 'json':
                schema = flex.load(file_json_name)
            print schema
        except ImportError as err:
            sys.stdout.write(str(err))
            log.warning(err)
        try:
            import SwaggerParser
            if args.format == 'yaml':
                parser = SwaggerParser(swagger_path=file_yaml_name)
            elif args.format == 'json':
                parser = SwaggerParser(swagger_path=file_json_name)
            print parser
        except ImportError as err:
            sys.stdout.write(str(err))
            log.warning(err)


if __name__ == '__main__':
    main()
