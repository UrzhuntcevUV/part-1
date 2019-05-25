def select(arr):
    count_compare = 0 # Счетчик сравнений
    count_move = 0    # Счетчик перемещений
    n = len(arr)      # Количество элементов в массиве

    for i in range(0, n):
        min = i # Индекс минимального элемента на текущем шаге

        for j in range(i+1, n):   # Перебор хвоста
            count_compare += 1    # Считаем количество сравнений 
            if arr[j] < arr[min]: # Находим минимальный элемент
                min = j           # Записываем индекс минимального элемента

        if min != i:
            # Если индекс минимального элемента не равен индексу текущего,
            # тогда меняем элементы местами
            arr[i], arr[min] = arr[min], arr[i]
            count_move += 1 # Считаем колчество перемещений
    
    return [count_compare, count_move]
import random
arry = [random.randint(0, 20) for i in range(20)]
print(arry)
select(arry)
print(arry)