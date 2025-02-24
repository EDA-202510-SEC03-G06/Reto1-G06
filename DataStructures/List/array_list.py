def new_list():
    newlist = {
        'elements': [],
        'size': 0,
    }
    return newlist

def get_element(my_list, index):
    return my_list["elements"][index]


def is_present(my_list, element, cmp_function):
    
    size = my_list["size"]
    if size > 0:
        keyexist = False
        for keypos in range(0, size):
            info = my_list["elements"][keypos]
            if cmp_function(element, info) == 0:
                keyexist = True
                break
        if keyexist:
            return keypos
    return -1


def add_first(my_list, element):
    #Agrega un elemento al inicio de la lista.
    #Inserta el elemento al inicio de la lista y actualiza el tamaño de la lista en 1.
     my_list['elements'] = [element] + my_list['elements']
     my_list['size'] += 1 
     return my_list
 
 
def add_last(my_list, element):
    #Agrega un elemento al final de la lista.
    #Inserta el elemento al final de la lista y aumenta el tamaño de la lista en 1.
    
     my_list['elements'].append(element)
     my_list['size'] += 1
     return my_list
 
 
def size(my_list):
    #Retorna el tamaño de la lista.
    
     return my_list['size']


def first_element(my_list):
    #Retorna el primer elemento de una lista no vacía.
    #Retorna el primer elemento de la lista. Si la lista está vacía, lanza un error index out of range.
    # Esta función no elimina el elemento de la lista.
    
    if my_list['size'] == 0:
        return "IndexError: list index out of range"
    return my_list['elements'][0]


def sub_list(my_list, pos_i, num_elements):
     
    if pos_i < 1 or pos_i > my_list["size"]:
        raise IndexError("list index out of range")

    sublist = {
        "elements": my_list["elements"][pos_i - 1: pos_i - 1 + num_elements],
        "size": min(num_elements, my_list["size"] - (pos_i - 1))
    }
    return sublist

def iterator(lst):
   
    return [element for element in lst] 