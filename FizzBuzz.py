"""
 Вы должны написать функцию, которая принимает положительное целое число и возвращает:
"Fizz Buzz", если число делится на 3 и 5;
"Fizz", если число делится на 3;
"Buzz", если число делится на 5;
Число, как строку для остальных случаев.

Входные данные: Число, как целочисленное (int).

Выходные данные: Ответ, как строка
"""


def checkio(number):
    if number % 3 == 0 and number % 5 == 0:
        return "Fizz Buzz"
    elif number % 3 == 0:
        return "Fizz"
    elif number % 5 == 0:
        return "Buzz"
    else:
        return str(number)


print(checkio(15) == "Fizz Buzz")

print(checkio(6) == "Fizz")

print(checkio(5) == "Buzz")

print(checkio(7) == "7")

