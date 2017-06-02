def reverse_chain(chain):
    if chain == None or chain.get('next') == None:
        return chain
    left, next = chain, chain['next'].get('next')
    chain = chain['next']
    left['next'] = None

    while True:
        chain['next'] = left
        if next == None:
            break
        left, chain, next = chain, next, next.get('next')
    return chain

def create_chain(len):
    node = {
        'value': None,
        'next': None
    }
    base_node = node
    for x in range(len):
        next = {
            'value': x,
            'next': None
        }
        node['next'] = next
        node = next
    return base_node

print(create_chain(5))
print(reverse_chain(create_chain(5)))
