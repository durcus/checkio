"""
Даны две строки со словами, разделенными запятыми. Попробуйте найти что общего между этими строками. Слова внутри каждой строки не повторяются.
Ваша функция должна находить все слова, которые появляются в обеих строках. Результат должен быть представлен, как строка со словами разделенными запятыми и отсортированными в алфавитном порядке.
Вх. данные: Два аргумента как строки (str).
Вых. данные: Общие слова как строка (str).
"""


def checkio(st1, st2):
    sp1 = st1.split(',')
    sp2 = st2.split(',')
    res = []
    for i in sp1:
        if i in sp2:
            res.append(i)
    res.sort()
    result = ','.join(res)
    return result


print(checkio("hello,world", "hello,earth") == "hello")
print(checkio("one,two,three", "four,five,six") == "")
print(checkio("one,two,three", "four,five,one,two,six,three") == "one,three,two")
