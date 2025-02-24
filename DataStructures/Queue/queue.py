def new_queue():
    return {'size': 0, 'elements': []}

def enqueue(my_queue, element):
    
    my_queue['elements'].append(element) 
    my_queue['size'] += 1  
    return my_queue  

def dequeue(my_queue):
    
    if my_queue['size'] == 0:
        raise Exception('EmptyStructureError: queue is empty')
    
    element = my_queue['elements'].pop(0)
    my_queue['size'] -= 1 
    return element 

def peek(my_queue):
    
    if my_queue['size'] == 0:
        raise Exception('EmptyStructureError: queue is empty') 

    return my_queue['elements'][0] 

def is_empty(my_queue):
    return my_queue['size'] == 0 

def size(my_queue):
    return my_queue['size'] 
