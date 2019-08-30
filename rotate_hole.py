
def rotate(state, pipe):
    result = []
    for i in range(len(state)):
        for k in pipe:
            if state[k] != 1:
                break
        else:
            result.append(i)
        state.insert(0, state.pop())
    print(result)
    return result


print(rotate([1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 1], [0, 1]) == [1, 8])
print(rotate([1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 1], [0, 1, 2]) == [])
print(rotate([1, 0, 0, 0, 1, 1, 0, 1], [0, 4, 5]) == [0])
print(rotate([1, 0, 0, 0, 1, 1, 0, 1], [5, 4, 5]) == [0, 5])

