def reverse_chain(chain):
    import copy
    chain = copy.deepcopy(chain)
    prev = None
    while True:
        next = chain.get('next')
        chain['next'] = prev
        if next == None:
            break
        prev, chain = chain, next
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
