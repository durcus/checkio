"""
Все слова в строковом представлении числа должны быть разделены одним пробелом. Будьте осторожны с пробелами -- очень сложно увидеть двойной пробел, но это критично для компьютера.

Вх. данные: Число, как целочисленное (int).
Вых. данные: Текстовое написание числа, как строка (str).
0 < number < 1000
"""


def checkio(number):
    list_numbers = ['one', 'two', 'three', 'four', 'five', 'six', 'seven',
                    'eight', 'nine']
    list_teens_numbers = ['ten', 'eleven', 'twelve', 'thirteen',
                          'fourteen', 'fifteen', 'sixteen', 'seventeen',
                          'eighteen', 'nineteen']
    list_ty_numbers = ['twenty', 'thirty', 'forty', 'fifty', 'sixty',
                       'seventy', 'eighty', 'ninety']
    lenght = len(str(number))
    test = number // 100
    test3 = number % 100
    test1 = test3 // 10
    test2 = number % 10
    if lenght == 1:
        return list_numbers[number - 1]
    elif lenght == 2:
        if test1 == 1:
            return list_teens_numbers[test2]
        else:
            if test2 == 0:
                return list_ty_numbers[test1 - 2]
            else:
                return list_ty_numbers[test1 - 2] + ' ' + list_numbers[test2 - 1]
    else:
        if test3 == 0:
            return list_numbers[test - 1] + ' hundred'
        elif test1 == 1:
            return list_numbers[test - 1] + ' hundred' + ' ' + list_teens_numbers[test2]
        elif test2 == 0:
            return list_numbers[test - 1] + ' hundred' + ' ' + list_ty_numbers[test1 - 2]
        elif test1 == 0:
            return list_numbers[test - 1] + ' hundred' + ' ' + list_numbers[test2 - 1]
        else:
            return list_numbers[test - 1] + ' hundred' + ' ' + list_ty_numbers[test1 - 2] + ' ' + list_numbers[test2 - 1]


print(checkio(4) == 'four')
print(checkio(143) == 'one hundred forty three')
print(checkio(12) == 'twelve')
print(checkio(101) == 'one hundred one')
print(checkio(212) == 'two hundred twelve')
print(checkio(40) == 'forty')
print(checkio(54) == 'fifty four')
print(checkio(400) == 'four hundred')
