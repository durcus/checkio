"""
 В этой миссии вам нужно реализовать несколько булевых операций:
• конъюнкция ("conjunction") обозначенная x ∧ y, удовлетворяющая условиям x ∧ y = 1 если x = y = 1 и x ∧ y = 0 иначе.
• дизъюнкция ("disjunction") обозначенная x ∨ y, удовлетворяющая условиям x ∨ y = 0 если x = y = 0 и x ∨ y = 1 иначе.
• импликация ("implication") (прямая импликация) обозначенная x→y и описанная как ¬ x ∨ y. Если x это истина, тогда значение x → y берётся такое, как y. Но если x — ложь, тогда результат будет истина без учёта значения y.
• исключение ("exclusive") (исключающее ИЛИ) обозначенное x ⊕ y и описанное как (x ∨ y)∧ ¬ (x ∧ y). Результат истина если x и y различны, и ложь в противном случае. В терминах арифметики, это сложение по модулю 2, где 1 + 1 = 0.
• эквивалентность ("equivalence") обозначенная x ≡ y и описанная как ¬ (x ⊕ y). Это истина, когда x и y имеют одинаковые значения.
Здесь вы можете увидеть таблицу истинности для данных операций:

 x | y | x∧y | x∨y | x→y | x⊕y | x≡y |
--------------------------------------
 0 | 0 |  0  |  0  |  1  |  0  |  1  |
 1 | 0 |  0  |  1  |  0  |  1  |  0  |
 0 | 1 |  0  |  1  |  1  |  1  |  0  |
 1 | 1 |  1  |  1  |  1  |  0  |  1  |
--------------------------------------

Даны два булевых значения x и y как 1 или 0, и дано имя операции, как описано ранее. Вы должны вычислить значение и вернуть его как 1 или 0.
Входные значения: Три аргумента. X и Y как 0 или 1. Имя операции, как строка.
Выходное значение: Результат как 1 или 0.
"""
# OPERATION_NAMES = ("conjunction", "disjunction", "implication", "exclusive", "equivalence")


def boolean(x, y, operation):
    if operation == "conjunction":
        return int(x and y)
    elif operation == "disjunction":
        return int(x or y)
    elif operation == "implication":
        if x:
            return y
        else:
            return 1
    elif operation == "exclusive":
        if x != y:
            return 1
        else:
            return 0
    elif operation == "equivalence":
        if x == y:
            return 1
        else:
            return 0


print(boolean(1, 0, "conjunction") == 0)
print(boolean(0, 1, "exclusive") == 1)
print(boolean(1, 0, "conjunction") == 0),  # "and"
print(boolean(1, 0, "disjunction") == 1),  # "or"
print(boolean(1, 1, "implication") == 1),  # "material"
print(boolean(0, 1, "exclusive") == 1),  # "xor"
print(boolean(0, 1, "equivalence") == 0),  # "same?"
