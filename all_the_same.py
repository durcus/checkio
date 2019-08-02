"""
все ли элементы массива равны.
Входные: List.
Выходные: Bool.
"""
from typing import List, Any


def all_the_same(elements: List[Any]) -> bool:
    if elements:
        a = elements[0]
        for i in elements[1:]:
            if i != a:
                return False
    return True


print(all_the_same([1, 1, 1]) == True)
print(all_the_same([1, 2, 1]))
print(all_the_same(['a', 'a', 'a']) == True)
print(all_the_same([]) == True)
