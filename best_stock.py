"""
 Вам даны текущие цены на акции. Вам необходимо выяснить за какие акции дают большую цену.

Input: Словарь (dict), в котором ключи - это рыночный код, а значение - это цена за акцию(float)

Output: Строка, рыночный код
"""


def best_stock(data):
    sp = data.values()
    m = max(sp)
    for key, value in data.items():
        if value == m:
            return key


print(best_stock({
    'CAC': 10.0,
    'ATX': 390.2,
    'WIG': 1.2
}))

print(best_stock({
    'CAC': 91.1,
    'ATX': 1.01,
    'TASI': 120.9
}))
