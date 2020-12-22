def solution(v):
    v.sort(key=lambda x: x[0])
    answer = []
    answer.append(v[0][0])
    for i in range(1, 3):
        if answer and v[i][0] == answer[-1]:
            answer.pop()
        else:
            answer.append(v[i][0])

    v.sort(key=lambda x: x[1])
    answer.append(v[0][1])
    for i in range(1, 3):
        if answer and v[i][1] == answer[-1]:
            answer.pop()
        else:
            answer.append(v[i][1])
    return answer

v1 = [[1, 4], [3, 10], [3, 4]]
v2 = [[1, 1], [2, 2], [1, 2]]
print(solution(v1))