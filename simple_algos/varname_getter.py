# coding: utf-8


def get_varname(var):
  """Return string name of variable"""
  import inspect
  frame = inspect.currentframe()
  var_id = id(var)
  for name in frame.f_back.f_locals.keys():
    try:
      if id(eval(name)) == var_id:
        return(name)
    except Exception as e:
      return "Error taken {}".format(str(e))
