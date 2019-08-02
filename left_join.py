"""
 Дана последовательность строк. Вы должны объединить эти строки в блок текста, разделив изначальные строки запятыми. В качестве шутки над праворукими роботами, вы должны заменить все вхождения слова "right" на слова "left", даже если это часть другого слова. Все строки даны в нижнем регистре.

Входные данные: Последовательность строк, как кортеж строк (юникод).

Выходные данные: Текст, как строка.
"""


def left_join(phrases):
    new_phrases = []
    for i in phrases:
        i = i.replace('right', 'left')
        new_phrases.append(i)
    return ','.join(new_phrases)


print(left_join(("left", "right", "left", "stop")) == "left,left,left,stop")
print(left_join(("bright aright", "ok")) == "bleft aleft,ok")
print(left_join(("brightness wright",)) == "bleftness wleft")
print(left_join(("enough", "jokes")) == "enough,jokes")
