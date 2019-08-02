"""
 Птичка меняет слова по следующим правилам:
    - после каждой согласной буквы она добавляет случайную гласную букву (l ⇒ la or le);
    - после каждой гласной буквы она добавляет две таких же буквы (a ⇒ aaa);
Гласные буквы == "aeiouy".
Вам дана птичья фраза как несколько слов, разделёных пробелами (каждая пара слов разделена одним пробелом). Птичка не знает ничего о знаках пунктуации и использует только буквы. Все слова даны в нижнем регистре. Необходимо перевести эту птичью песню в понятную простым роботам фразу.
Входные данные: Птичья фраза как строка (string).
Выходные данные: Перевод как строка (string).
"""
VOWELS = "aeiouy"


def translate(phrase):
    result = ''
    while phrase:
        if phrase[0] in VOWELS:
            result += phrase[0]
            phrase = phrase[3:]
        elif phrase[0] == ' ':
            result += phrase[0]
            phrase = phrase[1:]
        else:
            result += phrase[0]
            phrase = phrase[2:]
    return result


print(translate("hieeelalaooo") == "hello")
print(translate("hoooowe yyyooouuu duoooiiine") == "how you doin")
print(translate("aaa bo cy da eee fe") == "a b c d e f")
print(translate("sooooso aaaaaaaaa") == "sos aaa")
