"""
 Дан текст, который содержит различные английские буквы и знаки препинания. Вам необходимо найти самую частую букву в тексте. Результатом должна быть буква в нижнем регистре.
При поиске самой частой буквы, регистр не имеет значения, так что при подсчете считайте, что "A" == "a". Убедитесь, что вы не считайте знаки препинания, цифры и пробелы, а только буквы.
Если в тексте две и больше буквы с одинаковой частотой, тогда результатом будет буква, которая идет первой в алфавите. Для примера, "one" содержит "o", "n", "e" по одному разу, так что мы выбираем "e".
Вх. данные: Текст для анализа, как строка.
Вых. данные: Наиболее частая буква, как строка.
"""


def checkio(text: str) -> str:
    text = text.lower()
    number = 1
    result = []
    for i in text:
        if i.isalpha():
            if text.count(i) > number:
                number = text.count(i)
    for i in text:
        if i.isalpha():
            if text.count(i) == number:
                if i not in result:
                    result.append(i)
    result = sorted(result)
    return result[0]


print(checkio("Hello World!") == "l")
print(checkio("How do you do?") == "o")
print(checkio("One") == "e")
print(checkio("Oops!") == "o")
print(checkio("AAaooo!!!!") == "a")
print(checkio("abe") == "a")
print(checkio("Hello World!") == "l")
print(checkio("How do you do?") == "o")
print(checkio("One") == "e")
print(checkio("Oops!") == "o")
print(checkio("AAaooo!!!!") == "a")
print(checkio("abe") == "a")
print("Start the long test")
print(checkio("a" * 9000 + "b" * 1000) == "a")
