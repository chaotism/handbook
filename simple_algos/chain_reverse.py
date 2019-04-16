def reverse_chain(chain_ring):
    import copy
    chain_ring = copy.deepcopy(chain_ring)
    prev_ring = None
    while True:
        next_ring = chain_ring.get('next')
        chain_ring['next'] = prev_ring
        if next_ring == None:
            break
        prev_ring, chain_ring = chain_ring, next_ring
    return chain_ring

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
