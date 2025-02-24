def new_stack():
    return {'size': 0, 'first': None, 'last': None}

def push(my_stack, element):
    
    new_node = {'info': element, 'next': my_stack['first']}

    my_stack['first'] = new_node
    if my_stack['size'] == 0:
        my_stack['last'] = new_node 

    my_stack['size'] += 1

    return my_stack

def pop(my_stack):
    
    if my_stack['size'] == 0:
        raise Exception('EmptyStructureError: stack is empty')

    removed_element = my_stack['first']['info']

    my_stack['first'] = my_stack['first']['next']

    if my_stack['first'] is None:
        my_stack['last'] = None

    my_stack['size'] -= 1

    return removed_element

def is_empty(my_stack):
    return my_stack['size'] == 0

def top(my_stack):
   
    if my_stack['size'] == 0:
        raise Exception('EmptyStructureError: stack is empty')

    return my_stack['first']['info']

def size(my_stack):
    return my_stack['size']

def peek(stack):
    return top(stack)