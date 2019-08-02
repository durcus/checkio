"""
Помогите Николе разработать модуль для проверки паролей на безопасность. Пароль считается достаточно стойким, если его длина больше или равна 10 символам, он содержит, как минимум одну цифру, одну букву в верхнем и одну в нижнем регистре. Пароль может содержать только латинские буквы и/или цифры.
Вх. данные: Пароль как строка.
Вых. данные: Безопасность пароля в виде булевого значения (bool) или любого типа данных, который может быть сконвертирован и представлен как булево значение (True или False)
re.match("[a-zA-Z0-9]+", password)
"""


def checkio(data: str) -> bool:
    if len(data) < 10 or data.isdigit() or data.isalpha() or data.islower() or data.isupper():
        return False
    else:
        return True


print(checkio('A1213pokl') == False)
print(checkio('bAse730onE') == True)
print(checkio('asasasasasasasaas') == False)
print(checkio('QWERTYqwerty') == False)
print(checkio('123456123456') == False)
print(checkio('QwErTy911poqqqq') == True)
