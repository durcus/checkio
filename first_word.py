"""
 Дана строка и нужно найти ее первое слово.
При решении задачи обратите внимание на следующие моменты:
    В строке могут встречатся точки и запятые
    Строка может начинаться с буквы или, к примеру, с пробела или точки
    В слове может быть апостроф и он является частью слова
    Весь текст может быть представлен только одним словом и все
Входные параметры: Строка.
Выходные параметры: Строка.
"""


def first_word(text: str) -> str:
    sp = text.strip('.').split()
    if sp[0][-1] == ',' or sp[0][-1] == '.':
        return sp[0][:-1]
    elif '.' in sp[0]:
        w = sp[0].split('.')
        return w[0]
    else:
        return sp[0]


print(first_word("Hello world") == "Hello")
print(first_word(" a word ") == "a")
print(first_word("don't touch it") == "don't")
print(first_word("greetings, friends") == "greetings")
print(first_word("... and so on ...") == "and")
print(first_word("hi") == "hi")
print(first_word("Hello.World") == "Hello")
