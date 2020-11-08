def solution(n):
    answer = 0
    visited = [0]*(n+1)
    visited[0], visited[1] = 1, 1

    while visited.count(0):
        x = visited.index(0)
        cnt = 0
        for i in range(1, x+1):
            if x % i == 0:
                cnt += 1
            if cnt == 2:
                answer += 1
                break
        for v in range(1, n+1):
            if v % x == 0:
                visited[v] = 1

    return answer



n = 10
print(solution(n))
