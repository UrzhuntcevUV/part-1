from random import randint
from insert import insert
from select import select
from bubble import bubble

N = 10

def get_array(type='up'):
    if type == 'up':
        return [i for i in range(0, N)]
    
    if type == 'down':
        return [i for i in range(N - 1, -1, -1)]

    if type == 'rand':
        return [randint(0,N) for i in range(0, N)]

def check_sort():
    result = {
        'insert': {},
        'select': {},
        'bubble': {},
    }
    array_insert = get_array('up')
    array_select = array_insert.copy()
    array_bubble = array_insert.copy()
    result['insert']['up'] = insert(array_insert, len(array_insert))
    result['select']['up'] = select(array_select)
    result['bubble']['up'] = bubble(array_bubble)

    array_insert = get_array('down')
    array_select = array_insert.copy()
    array_bubble = array_insert.copy()
    result['insert']['down'] = insert(array_insert, len(array_insert))
    result['select']['down'] = select(array_select)
    result['bubble']['down'] = bubble(array_bubble)
    
    
    avg = {
        'insert': [0, 0],
        'select': [0, 0],
        'bubble': [0, 0]
    }
    for i in range(400):
        array_insert = get_array('rand')
        array_select = array_insert.copy()
        array_bubble = array_insert.copy()
        
        sort_result = insert(array_insert, len(array_insert))
        avg['insert'][0] += sort_result[0]
        avg['insert'][1] += sort_result[1]

        sort_result = select(array_select)
        avg['select'][0] += sort_result[0]
        avg['select'][1] += sort_result[1]

        sort_result = bubble(array_bubble)
        avg['bubble'][0] += sort_result[0]
        avg['bubble'][1] += sort_result[1]

    result['insert']['rand'] = [avg['insert'][0]/400, avg['insert'][1]/400]
    result['select']['rand'] = [avg['select'][0]/400, avg['select'][1]/400]
    result['bubble']['rand'] = [avg['bubble'][0]/400, avg['bubble'][1]/400]

    return result

print( check_sort() )