def solution(arr):
    answer = []
    answer.append(arr[0])
    a_index = 0
    for i in range(1, len(arr)):
        if arr[i] != answer[a_index]:
            answer.append(arr[i])
            a_index += 1

    return answer

print(solution([1,1,3,3,0,1,1]))
