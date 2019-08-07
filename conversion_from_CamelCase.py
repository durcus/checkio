"""
 Ваша задача - написать функцию, которая преобразовывает текст (название другой функции) из формата CamelCase, принятого в JavaScript (MyFunctionName) в формат, принятый в Python (my_function_name), где все буквы - маленькие, а слова соединены знаком нижнего подчеркивания "_".

Входные данные: Название функции как строка в CamelCase
Output: То же самое название, но в under_score
"""


def from_camel_case(name):
    result_list = []
    while name:
        for i in range(1, len(name)):
            if name[i].isupper():
                result_list.append(name[:i].lower())
                name = name[i:]
                break
            elif i == len(name) - 1:
                result_list.append(name.lower())
                name = ''
    result = '_'.join(result_list)
    return result


print(from_camel_case("MyFunctionName") == "my_function_name")
print(from_camel_case("IPhone") == "i_phone")
print(from_camel_case("ThisFunctionIsEmpty") == "this_function_is_empty")
print(from_camel_case("Name") == "name")
