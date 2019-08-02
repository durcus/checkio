"""
 На вход Вашей функции будет передано одно предложение. Необходимо вернуть его исправленную копию так, чтобы оно всегда начиналось с большой буквы и заканчивалось точкой.

Обратите внимание на то, что не все исправления необходимы. Если предложение уже заканчивается на точку, то добавлять еще одну не нужно, это будет ошибкой

Входные аргументы: Строка (A string).

Выходные аргументы: Строка (A string).
"""


def correct_sentence(text):
    first = text[0].upper()
    text = first + text[1:]
    if text[-1] != '.':
        text = text + '.'
    return text


print(correct_sentence("greetings, friends") == "Greetings, friends.")
print(correct_sentence("Greetings, friends") == "Greetings, friends.")
print(correct_sentence("Greetings, friends.") == "Greetings, friends.")
print(correct_sentence("hi") == "Hi.")
print(correct_sentence("welcome to New York") == "Welcome to New York.")
