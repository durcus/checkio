"""
Вам дан результат игры, и вы должны решить, кто победил или что это ничья. Ваша функция должна вернуть "X" если победил Х-игрок и "О" если победил О-игрок. В случае ничьи, результат должен быть "D".
 Результаты игры представлены, как список (list) строк, где "X" и "O" - это отметки игроков и "." - это пустая клетка.
Вх. данные: Результат игры, как список (list) строк (str, unicode).
Вых. данные: "X", "O" или "D", как строка (str).
"""


def checkio(game_result):
    for i in range(3):
        if game_result[i][0] == game_result[i][1] and\
           game_result[i][2] == game_result[i][1] and\
           game_result[i][0] != '.':
            return game_result[i][0]
    for j in range(3):
        if game_result[0][j] == game_result[1][j] and\
           game_result[1][j] == game_result[2][j] and\
           game_result[0][j] != '.':
            return game_result[0][j]
    if (game_result[1][1] == game_result[0][0] == game_result[2][2] or
        game_result[1][1] == game_result[0][2] == game_result[2][0]) and\
       game_result[1][1] != '.':
        return game_result[1][1]
    else:
        return 'D'


print(checkio([
    "X.O",
    "XX.",
    "XOO"]) == "X")
print(checkio([
    "OO.",
    "XOX",
    "XOX"]) == "O")
print(checkio([
    "OOX",
    "XXO",
    "OXX"]) == "D")
