"""
Я начал кормить одного из голубей. Через минуту прилетело еще два, и еще через минуту прилетело еще три голубя. Затем 4 и так далее (Пр: 1+2+3+4+...). Одной порции корма хватает одному голубю на минуту. В случае если еды не хватает на всех птиц, то сначала едят те голуби, что прилетели ранее. Голуби - это вечно голодные птицы и они будут есть и есть без остановки. Если у меня есть number порций корма, то сколько голубей я смогу покормить хотя бы по разу?
Входные данные: Количество порций корма, как целое число (int).
Выходные данные: Количество накормленных голубей, как целое число (int).
"""


def checkio(number):
    result = 0
    m = number
    for i in range(m):
        result += (i + 1)
        if number == result:
            return result
        elif number < result:
            result -= (i + 1)
            if result < number:
                result += (number - result)
                return result
            else:
                return result
        else:
            number -= result


print(checkio(1) == 1)
print(checkio(2) == 1)
print(checkio(5) == 3)
print(checkio(10) == 6)
print(checkio(3) == 2)
