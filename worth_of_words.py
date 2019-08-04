"""
У вас есть список слов и ваша задача - определить самое ценное из них. То, которое принесет больше всего очков.
Правила:
Каждое слово имеет ценность, которая эквивалентна сумме очков всех букв, входящих в него.
Стоимость букв следующая:
e, a, i, o, n, r, t, l, s, u = 1
d, g = 2
b, c, m, p = 3
f, h, v, w, y = 4
k = 5
j, x = 8
q, z = 10
Например, ценность слова 'dog' - 5, так как 'd' = 2, 'o' = 1 и 'g' = 2.
"""


def worth_of_words(words):
    num = 0
    res_list = []
    for i in words:
        for k in i:
            if k == 'e' or k == 'a' or k == 'i' or k == 'o' or k == 'n'\
               or k == 'r' or k == 't' or k == 'l' or k == 's' or k == 'u':
                num += 1
            elif k == 'd' or k == 'g':
                num += 2
            elif k == 'b' or k == 'c' or k == 'm' or k == 'p':
                num += 3
            elif k == 'f' or k == 'h' or k == 'v' or k == 'w' or k == 'y':
                num += 4
            elif k == 'k':
                num += 5
            elif k == 'j' or k == 'x':
                num += 8
            elif k == 'q' or k == 'z':
                num += 10
        res_list.append(num)
        num = 0
    res_num = max(res_list)
    return words[res_list.index(res_num)]


print(worth_of_words(['hi', 'quiz', 'bomb', 'president']) == 'quiz')
print(worth_of_words(['zero', 'one', 'two',
                      'three', 'four', 'five']) == 'zero')
