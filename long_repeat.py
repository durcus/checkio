"""
Вам необходимо найти длину самой длинной подстроки, которая состоит из одинаковых букв. Например, строка "aaabbcaaaa" состоит из четырех подстрок с одинаковыми буквами "aaa", "bb","c" и "aaaa". Последняя подстрока является самой длинной, что и делает ее ответом.
Входные данные: Строка.
Выходные данные: Целое число.
"""


def long_repeat(line):
    if line:
        result = 1
        real = 1
        x = line[0]
        for i in line[1:]:
            if i == x:
                real += 1
                if real > result:
                    result = real
            else:
                real = 1
                x = i
        return result
    else:
        return 0


print(long_repeat('sdsffffse') == 4)
print(long_repeat('ddvvrwwwrggg') == 3)
print(long_repeat('sdsffffse') == 4)
print(long_repeat('ddvvrwwwrggg') == 3)
print(long_repeat('abababaab') == 2)
print(long_repeat('') == 0)
print(long_repeat('aa') == 2)
print(long_repeat('zxcvbnmasdfgh') == 1)
