def start(N):
    for i in range(N):
        for j in range(N):
            if arr[i][j] == '2':
                return i, j


def maze(i, j, N):
    if arr[i][j] == '3':
        return 1
    else:
        v[i][j] = 1
        for di, dj in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            ni, nj = i+di, j+dj
            if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] != '1' and v[ni][nj] == 0:
                if maze(ni, nj, N):
                    return 1
        return 0

#-------------------------------------
T = int(input())
for tc in range(1, 1+T):
    N = int(input())
    arr = [input() for _ in range(N)]
    v = [[0]*N for _ in range(N)]
    (i, j) = start(N)
    print(f'#{tc} {maze(i, j, N)}')