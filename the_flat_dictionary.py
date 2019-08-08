"""
 Словари - это удобный тип данных для хранения и обработки различных конфигураций. Они позволяют хранить данные по ключам и создавать вложенные структуры. Дан словарь, в котором в качестве ключей используются строки, а в качестве значений строки или словари. Необходимо сделать этот словарь "плоским", но сохранить структуру в ключах. Результатом будет словарь без вложенных словарей. Ключи должны содержать путь, составленный из родительских ключей из начального словаря, разделенных "/". Если значение ключа есть пустой словарь, тогда оно должно быть заменено пустой строкой (""). Взглянем на пример:

{
    "name": {
        "first": "One",
        "last": "Drone"
    },
    "job": "scout",
    "recent": {},
    "additional": {
        "place": {
            "zone": "1",
            "cell": "2"}
    }
}

 Результатом будет:

{"name/first": "One",           #один прародитель
 "name/last": "Drone",
 "job": "scout",                #ключ корневого уровня
 "recent": "",                  #пустой словарь
 "additional/place/zone": "1",  #третий уровень
 "additional/place/cell": "2"}
"""


def flatten(dictionary):
    result = {}
    while dictionary:
        for i in dictionary:
            if dictionary[i] == {}:
                result.update({i: ""})
            elif type(dictionary[i]) != dict:
                result.update({i: dictionary[i]})
        for k in result:
            if k in dictionary:
                del dictionary[k]
        test = {}
        for l, m in dictionary.items():
            for x in m:
                test.update({(l + '/' + x): m[x]})
        dictionary = test
    return result


print(flatten({"key": "value"}) == {"key": "value"})  # "Simple"
print(flatten(
    {"key": {"deeper": {"more": {"enough": "value"}}}}
) == {"key/deeper/more/enough": "value"})             # "Nested"
print(flatten({"empty": {}}) == {"empty": ""})        # "Empty value"
print(flatten({"name": {
    "first": "One",
    "last": "Drone"},
    "job": "scout",
    "recent": {},
    "additional": {
    "place": {
        "zone": "1",
        "cell": "2"}}}
) == {"name/first": "One",
      "name/last": "Drone",
                    "job": "scout",
                    "recent": "",
                    "additional/place/zone": "1",
                    "additional/place/cell": "2"})
print(flatten({"key": "value"}) == {"key": "value"})
print(flatten({"key": {"deeper": {"more": {"enough": "value"}}}}) == {
    "key/deeper/more/enough": "value"})
print(flatten({"empty": {}}) == {"empty": ""})
