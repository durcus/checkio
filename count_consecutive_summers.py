"""
 Положительные целые числа могут быть выражены в виде сумм последовательных положительных целых чисел различными способами. Например, 42 можно выразить как такую сумму четырьмя различными способами: (а) 3+4+5+6+7+8+9, (б) 9+10+11+12, (в) 13+14+15 и (г) 42. Как показывает последнее решение (г), любое положительное целое число всегда можно тривиально выразить в виде одноэлементной суммы, состоящей только из этого целого числа.
Вычислите, каким количеством различных способов это можно выразить как сумму последовательных положительных чисел.
Входные данные: Целое число (Int).
Выходные данные: Целое число (Int).
"""


def count_consecutive_summers(num):
    test = [i for i in range(1, num)]
    summa = 0
    counter = 1
    for i in range(num - 1):
        for k in range(i, num - 1):
            summa += test[k]
            if summa == num:
                counter += 1
                summa = 0
                break
            if summa > num:
                summa = 0
                break
    print(counter)
    return counter


print(count_consecutive_summers(42) == 4)
print(count_consecutive_summers(99) == 6)
print(count_consecutive_summers(1) == 1)
print(count_consecutive_summers(3) == 2)
print(count_consecutive_summers(2) == 1)
