"""
 Дана таблица всех доступных продуктов на складе. Данные представлены в виде списка словарей (a list of dicts)
Ваша миссия тут - это найти ТОП самых дорогих товаров. Количество товаров, которые мы ищем, будет передано в первом аргументе, а сами данные по товарам будут переданы вторым аргументом.
Вх. данные: Число и список словарей (int and list of dicts). Каждый словарь имеет 2 ключа "name" и "price".
Вых. данные: Такой же как и второй аргумент.
"""


def bigger_price(limit: int, data: list) -> list:
    price = []
    for i in data:
        price.append(i['price'])
    price = sorted(price, reverse=True)
    bigger = []
    while limit:
        for i in data:
            if i['price'] == price[0]:
                bigger.append(i)
                limit -= 1
        del price[0]
    return bigger


print(bigger_price(2, [
    {"name": "bread", "price": 100},
    {"name": "wine", "price": 138},
    {"name": "meat", "price": 15},
    {"name": "water", "price": 1}
]) == [
    {"name": "wine", "price": 138},
    {"name": "bread", "price": 100}
])
print(bigger_price(1, [
    {"name": "pen", "price": 5},
    {"name": "whiteboard", "price": 170}
]) == [{"name": "whiteboard", "price": 170}])
