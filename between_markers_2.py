"""
 Вам дана строка и два маркера (начальный и конечный). Вам необходимо найти текст, заключенный между двумя этими маркерами. Но есть несколько важных условий:
    Начальный и конечный маркеры всегда разные
    Если нет начального маркера, то началом считать начало строки
    Если нет конечного маркера, то концом считать конец строки
    Если нет ни конечного, ни начального маркеров, то просто вернуть всю строку
    Если конечный маркер стоит перед начальным, то вернуть пустую строку
Input: Три аргумента. Все строки. Второй и третий аргументы это начальный и конечный маркеры.
Output: Строка.
"""


def between_markers(text: str, begin: str, end: str) -> str:
    if begin not in text and end not in text:
        return text
    elif begin not in text:
        return text[:text.find(end)]
    elif end not in text:
        return text[text.find(begin) + len(begin):]
    else:
        return text[text.find(begin) + len(begin):text.find(end)]


print(between_markers('What is >apple<', '>', '<') == "apple")
print(between_markers("<head><title>My new site</title></head>",
                      "<title>", "</title>") == "My new site")
print(between_markers('No[/b] hi', '[b]', '[/b]') == 'No')
print(between_markers('No [b]hi', '[b]', '[/b]') == 'hi')
print(between_markers('No hi', '[b]', '[/b]') == 'No hi',)
print(between_markers('No <hi>', '>', '<') == '')
