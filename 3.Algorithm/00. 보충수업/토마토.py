from collections import deque

def tomato(N, M):
    v = [[0] * M for _ in range(N)]
    q = deque()
    last = 0
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 1:
                q.append((i, j))
                v[i][j] = 1

    while q:
        i, j = q.popleft()
        for di, dj in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
            ni, nj = i+di, j+dj
            if 0 <= ni < N and 0 <= nj < M:
                if arr[ni][nj] == 0 and v[ni][nj] == 0:
                    q.append((ni, nj))
                    v[ni][nj] = v[i][j] + 1
                    last = v[i][j]
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 0 and v[i][j] == 0:
                return -1
    return last

#-----------------------------------------------------
M, N = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
print(tomato(N, M))


