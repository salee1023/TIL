def f(N):
    q = [(0, 0)]
    d = [[987654321]*N for _ in range(N)]
    d[0][0] = arr[0][0]
    while q:
        i, j = q.pop(0)
        for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            ni, nj = i+di, j+dj
            if 0 <= ni < N and 0 <= nj < N:
                cost = d[i][j] + arr[ni][nj]
                if d[ni][nj] > cost:
                    d[ni][nj] = cost
                    q.append((ni, nj))

    return d[N-1][N-1]
# ------------------------------------------------------
T = int(input())
for tc in range(1, 1+T):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    r = f(N)
    print(f'#{tc} {r}')