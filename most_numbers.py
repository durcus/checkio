"""
 Дан массив чисел (float или/и int). Вам нужно найти разницу между самым большим (максимум) и самым малым (минимум) элементом. Ваша функция должна уметь работать с неопределенным количеством аргументов. Если аргументов нет, то функция возвращает 0 (ноль).

Числа с плавающей точкой представлены в компьютерах как двоичная дробь. Результат проверяется с точностью до третьего знака, как ±0.001
Прочитайте о том как работать с переменым числом аргументов.

Вх. данные: Переменное число аргументов как числа (int, float).

Вых. данные: Разница между максимумом и минимумом как число (int, float).
"""


def checkio(*args):
    if len(args) == 0:
        return 0
    else:
        return round(max(args) - min(args), 3)


print(checkio(1, 2, 3) == 2)
print(checkio(5, -5) == 10)
print(checkio(10.2, -2.2, 0, 1.1, 0.5) == 12.4)
print(checkio() == 0)

