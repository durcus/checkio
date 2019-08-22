"""
зашифровать текст сообщения (в исходных данных не будет специальных символов вроде "!", "&", "?", только текст и пробелы) используя шифр Цезаря где каждая буква исходного текста заменяется другой, которая находится на определенном расстоянии в алфавите. Например, ("a b c", 3) == "d e f"
 Входные данные: Секретное сообщение как строка (только маленькие буквы и пробелы)
Output: Тот же самый текст, но зашифрованный
"""


def to_encrypt(sent, num):
    result = ''
    for i in sent:
        if i.isalpha():
            x = ord(i) + num
            if x > 122:
                x -= 26
            elif x < 97:
                x += 26
            result += chr(x)
        else:
            result += ' '
    return result


print(to_encrypt("a b c", 3) == "d e f")
print(to_encrypt("a b c", -3) == "x y z")
print(to_encrypt("simple text", 16) == "iycfbu junj")
print(to_encrypt("important text", 10) == "swzybdkxd dohd")
print(to_encrypt("state secret", -13) == "fgngr frperg")
