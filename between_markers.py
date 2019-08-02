"""
 Вам дана строка и два маркера (начальный и конечный). Вам необходимо найти текст, заключенный между двумя этими маркерами. Но есть несколько важных условий.
    Начальный и конечный маркеры всегда разные.
    Начальный и конечный маркеры всегда размером в один символ.
    Начальный и конечный маркеры всегда есть в строке и идут один за другим.
Input: Три аргумента. Все строки. Второй и третий аргументы это начальный и конечный маркеры.
Output: Строка.
"""


def between_markers(text: str, begin: str, end: str) -> str:
    return text[text.find(begin) + 1:text.find(end)]


print(between_markers('What is >apple<', '>', '<') == 'apple')
print(between_markers('What is >apple<', '>', '<') == "apple")
print(between_markers('What is [apple]', '[', ']') == "apple")
print(between_markers('What is ><', '>', '<') == "")
print(between_markers('>apple<', '>', '<') == "apple")
