"""
Вам необходимо найти первую самую длинную подстроку состоящую исключительно из неповторяющихся букв. Например, в строке "abca" мы имеем две подстроки с неповторяющимися буквами "abc" и "bca", но нам нужна первая подстрока, поэтому ответом будет "abc".
Входные данные: Строка.
Выходные данные: Строка.
"""


def non_repeat(line):
    result = ''
    lresult = ['']
    if len(line) > 1:
        while line:
            for i in line:
                if i not in result:
                    result += i
                else:
                    if len(result) > len(lresult[0]):
                        lresult[0] = result
                    result = ''
                    break
            line = line[1:]
        return lresult[0]
    else:
        return line


print(non_repeat('aaaaa') == 'a')
print(non_repeat('abdjwawk') == 'abdjw')
print(non_repeat('abcabcffab') == 'abcf')
print(non_repeat('w') == 'w')
