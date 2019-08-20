"""
 В начале игры, они кладут несколько черных и белых жемчужин в одну коробку. На каждый ход, игрок берет жемчужину из коробки и кладет обратно жемчужину другого цвета. Побеждает тот, кто вытаскивает белую жемчужину на N-ом шаге.
Но Роботы не любят неопределенностей и предпочтут знать вероятность белой жемчужины на нужном шаге. Вероятность - это значение от 0 (0% шанс и что этого точно не будет) до 1 (100% шанс или это точно случится). Результат должен быть числом от 0 до 1 с точностью до 2-ого знака (±0.01).
Дана информация о начальном наборе жемчужин, как строка из "b" (черная) и "w" (белая) и количество итераций (N). Порядок жемчужин не важен.
Input: Стартовая последовательность жемчужин, как строк (str) и число итераций, как целое число (int).
Output: Вероятность вытащить белую жемчужину, как число (float).
Предусловия: 0 < N ≤ 20
0 < len(pearls) ≤ 20
"""


def checkio(pearls, itera):
    pearls_l = [pearls]
    pt = []
    var = [1]
    vt = []
    r = len(pearls)
    if itera == 1:
        w = pearls.count('w')
        return w / r
    for i in range(itera - 1):
        for k in range(len(pearls_l)):
            w = pearls_l[k].count('w')
            b = pearls_l[k].count('b')
            if w > b:
                vt.append(var[k] * (w / r))
                vt.append(var[k] * (b / r))
                w -= 1
                b += 1
                s = 'w' * w + 'b' * b
                pt.append(s)
                if b > 1:
                    w += 2
                    b -= 2
                    s = 'w' * w + 'b' * b
                    pt.append(s)
                else:
                    s = ''
                    pt.append(s)
            elif w < b:
                vt.append(var[k] * (b / r))
                vt.append(var[k] * (w / r))
                b -= 1
                w += 1
                s = 'w' * w + 'b' * b
                pt.append(s)
                if w > 1:
                    b += 2
                    w -= 2
                    s = 'w' * w + 'b' * b
                    pt.append(s)
                else:
                    s = ''
                    pt.append(s)
            else:
                vt.append(var[k] * (b / r))
                vt.append(var[k] * (w / r))
                b -= 1
                w += 1
                s = 'w' * w + 'b' * b
                pt.append(s)
                if w > 1:
                    b += 2
                    w -= 2
                    s = 'w' * w + 'b' * b
                    pt.append(s)
                else:
                    s = ''
                    pt.append(s)
        var = vt
        vt = []
        pearls_l = pt
        pt = []
    result = 0
    for i in range(len(pearls_l)):
        if pearls_l[i]:
            w = pearls_l[i].count('w')
            result += (w / r) * var[i]
    return round(result, 2)


print(checkio('bbw', 3) == 0.48)
print(checkio('wwb', 3) == 0.52)
print(checkio('www', 3) == 0.56)
print(checkio('bbbb', 1) == 0)
print(checkio('wwbb', 4) == 0.5)
print(checkio('bwbwbwb', 5) == 0.48)
