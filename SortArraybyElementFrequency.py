"""
Отсортируйте заданную итерацию так, чтобы ее элементы оказались в порядке убывания частоты, то есть, сколько раз они появляются в элементах. Если два элемента имеют одинаковую частоту, они должны заканчиваться в том же порядке, что и первое появление в итерируемом.
 Input: Iterable
Output: Iterable
"""


def frequency_sort(items):
    data1 = []
    while items:
        number = items.count(items[0])
        ext = items[0]
        for i in items[1:]:
            if items.count(i) > number:
                number = items.count(i)
                ext = i
        for i in items:
            if items.count(i) == number and i == ext:
                data1.append(i)
        for i in range(number):
            items.remove(ext)
    return data1


print(list(frequency_sort([4, 6, 2, 2, 6, 4, 4, 4]))
      == [4, 4, 4, 4, 6, 6, 2, 2])
print(list(frequency_sort(['bob', 'bob', 'carl', 'alex', 'bob'])) == [
      'bob', 'bob', 'bob', 'carl', 'alex'])
print(list(frequency_sort([17, 99, 42])) == [17, 99, 42])
print(list(frequency_sort([])) == [])
print(list(frequency_sort([1])) == [1])
print(frequency_sort([17, 99, 42]) == [17, 99, 42])
print((frequency_sort([])) == [])
print((frequency_sort([1])) == [1])
