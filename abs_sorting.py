"""
 Массив (tuple) содержит различные числа. Вам необходимо отсортировать их, но отсортировать на основе абсолютных значений в возрастающем порядке. Для примера, последовательность (-20, -5, 10, 15) будет отсортирована следующим образом (-5, 10, 15, -20). Ваша функция должна возвращать список (list) или кортеж (tuple).

Входные данные: Массив чисел как кортеж (tuple).

Выходные данные: Список (list) или кортеж (tuple) (но не генератор) отсортированный по абсолютным значениям чисел.
Предусловия: len(set(abs(x) for x in array)) == len(array)
0 < len(array) < 100
all(isinstance(x, int) for x in array)
all(-100 < x < 100 for x in array)
"""


def checkio(numbers_array: tuple) -> list:
    my_sort = sorted([abs(x) for x in numbers_array])
    new_sort = []
    for i in my_sort:
        if i in numbers_array:
            new_sort.append(i)
        else:
            new_sort.append(-i)
    return new_sort


print(checkio((-20, -5, 10, 15)) == [-5, 10, 15, -20])
print(checkio((1, 2, 3, 0)) == [0, 1, 2, 3])
print(checkio((-1, -2, -3, 0)) == [0, -1, -2, -3])
