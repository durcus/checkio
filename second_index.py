"""
 Даны 2 строки. Необходимо найти индекс второго вхождения второй строки в первую.

Разберем самый первый пример, когда необходимо найти второе вхождение "s" в слове "sims". Если бы нам надо было найти ее первое вхождение, то тут все просто: с помощью функции index или find мы можем узнать, что "s" – это самый первый символ в слове "sims", а значит индекс первого вхождения равен 0. Но нам необходимо найти вторую "s", а она 4-ая по счету. Значит индекс второго вхождения (и ответ на вопрос) равен 3.

Input: Две строки (String).

Output: Int or None
"""


def second_index(text, symbol):
    if text.count(symbol) < 2:
        return None
    else:
        number = 0
        index = 0
        for i in text:
            if i == symbol:
                number += 1
                if number == 2:
                    return index
            index += 1


print(second_index("sims", "s") == 3)
print(second_index("find the river", "e") == 12)
print(second_index("hi", " ") is None)
print(second_index("hi mayor", " ") is None)
print(second_index("hi mr Mayor", " ") == 5)
