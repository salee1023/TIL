def f(i, j):
    v = [[0]*N for _ in range(N)]
    q = []
    q.append((i,j))
    v[i][j] = 1
    while q:
        i, j = q.pop(0)
        for di, dj in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            ni, nj = i+di, j+dj
            if 0 <= ni < N and 0 <= nj < N:
                if arr[ni][nj] != '1' and v[ni][nj] == 0:
                    q.append((ni, nj))
                    v[ni][nj] = v[i][j] + 1
                if arr[ni][nj] == '3':
                    return v[ni][nj]-2
    return 0

#---------------------------------------
T = int(input())
for tc in range(1, 1+T):
    N = int(input())
    arr = [input() for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if arr[i][j] == '2':
                si, sj = i, j

    print(f'#{tc} {f(si, sj)}')

