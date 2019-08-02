"""
 Дана строка со словами и числами, разделенными пробелами (один пробел между словами и/или числами). Слова состоят только из букв. Вам нужно проверить есть ли в исходной строке три слова подряд. Для примера, в строке "start 5 one two three 7 end" есть три слова подряд.
Входные данные: Строка со словами (str).
Выходные данные: Ответ как логическое выражение (bool), True или False.
"""


def checkio(words: str) -> bool:
    sp = words.split()
    number = 0
    for i in sp:
        if not i.isdigit():
            number += 1
            if number >= 3:
                return True
        else:
            number = 0
    return False


print(checkio("Hello World hello"))  # True
print(checkio("He is 123 man"))  # False
print(checkio("1 2 3 4"))  # False
print(checkio("bla bla bla bla"))  # True
print(checkio("Hi"))  # False

