def solution(rows, columns, swipes):
    # arr 행렬 초기화
    arr = [[0]*columns for _ in range(rows)]
    x = 1
    for i in range(rows):
        for j in range(columns):
            arr[i][j] = x
            x += 1

    answer = []
    for swipe in swipes:
        if swipe[0] == 1:
            tmp_answer = 0
            for j in range(swipe[2]-1, swipe[4]):
                tmp = arr[swipe[3]-1][j]
                for i in range(swipe[3]-2, swipe[1]-2, -1):
                    arr[i+1][j] = arr[i][j]
                arr[swipe[1]-1][j] = tmp
                tmp_answer += tmp
            answer.append(tmp_answer)
        elif swipe[0] == 2:
            tmp_answer = 0
            for j in range(swipe[2] - 1, swipe[4]):
                tmp = arr[swipe[3] - 1][j]
                for i in range(swipe[3] - 2, swipe[1] - 2, -1):
                    arr[i + 1][j] = arr[i][j]
                arr[swipe[1] - 1][j] = tmp
                tmp_answer += tmp
            answer.append(tmp_answer)
        elif swipe[0] == 3:
            tmp_answer = 0
            for i in range(swipe[1] - 1, swipe[3]):
                tmp = arr[i][swipe[4]-1]
                for j in range(swipe[4] - 2, swipe[2] - 2, -1):
                    arr[i][j+1] = arr[i][j]
                arr[i][swipe[2]-1] = tmp
                tmp_answer += tmp
            answer.append(tmp_answer)
        else:
            pass

    return arr


print(solution(4, 3, [[1,1,2,4,3],[3,2,1,2,3],[4,1,1,4,3],[2,2,1,3,3]]))