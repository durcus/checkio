"""
 Каждая цифра в написании времени представлена разным количеством бинарных знаков. Первая цифра в "часах" состоит из двух знаков, тогда как вторая цифра -- из четырех. Первая цифра "минут" и "секунд" состоят из трех знаков и вторые цифры -- из четырех. Каждая цифра должна быть переведена в двоичный вид. Затем замените каждую единицу (1) на тире ("-") и каждый ноль (0) на точку (".").
  Время может быть представлено в следующем виде: "hh:mm:ss", "h:m:s" или "hh:m:ss" "Пропущеные" цифры - это нули. Для примера, "1:2:3" тоже самое, что и "01:02:03".
Окончательная морзе-форма времени должна быть написана в следующем формате:
"h h : m m : s s"
где каждая цифра - это последовательность "." и "-"
Ввод: Нормальная запись времени, представленая строкой (str).
Вывод: Переработаная морзе-форма времени, представленая строкой (str).
"""


def checkio(time_string):
    result = ''
    time_list = time_string.split(":")
    for i in range(len(time_list)):
        if len(time_list[i]) == 1:
            time_list[i] = '0' + time_list[i]
    h = bin(int(time_list[0][0]))[2:]
    if len(h) == 1:
        h = '0' + h
    for k in h:
        if int(k) == 0:
            result += '.'
        else:
            result += '-'
    result += ' '
    h = bin(int(time_list[0][1]))[2:]
    if len(h) < 4:
        h = '0' * (4 - len(h)) + h
    for k in h:
        if int(k) == 0:
            result += '.'
        else:
            result += '-'
    result += ' : '
    h = bin(int(time_list[1][0]))[2:]
    if len(h) < 3:
        h = '0' * (3 - len(h)) + h
    for k in h:
        if int(k) == 0:
            result += '.'
        else:
            result += '-'
    result += ' '
    h = bin(int(time_list[1][1]))[2:]
    if len(h) < 4:
        h = '0' * (4 - len(h)) + h
    for k in h:
        if int(k) == 0:
            result += '.'
        else:
            result += '-'
    result += ' : '
    h = bin(int(time_list[2][0]))[2:]
    if len(h) < 3:
        h = '0' * (3 - len(h)) + h
    for k in h:
        if int(k) == 0:
            result += '.'
        else:
            result += '-'
    result += ' '
    h = bin(int(time_list[2][1]))[2:]
    if len(h) < 4:
        h = '0' * (4 - len(h)) + h
    for k in h:
        if int(k) == 0:
            result += '.'
        else:
            result += '-'
    return result


print(checkio("10:37:49") == ".- .... : .-- .--- : -.. -..-")
print(checkio("21:34:56") == "-. ...- : .-- .-.. : -.- .--.")
print(checkio("00:1:02") == ".. .... : ... ...- : ... ..-.")
print(checkio("23:59:59") == "-. ..-- : -.- -..- : -.- -..-")
