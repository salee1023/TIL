def phone(s): # s: start
    Q = [s]
    visited = [0]*101
    visited[s] = 1
    while Q:
        n = Q.pop(0)
        for i in range(1, 101):
            if adj[n][i] == 1 and visited[i] == 0:
                Q.append(i)
                visited[i] = visited[n] + 1
    else:
        max = 0
        res = 0
        for j in range(101):
            if visited[j] >= max:
                max = visited[j]
                res = j
        return res
# ----------------------------------------------
for tc in range(1,11):
    L, S = map(int, input().split())
    numbers = list(map(int, input().split()))
    adj = [[0]*101 for _ in range(101)]
    for i in range(L//2):
        adj[numbers[2*i]][numbers[2*i+1]] = 1 # 방향성 그래프
    print(f'#{tc} {phone(S)}')