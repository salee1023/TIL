def f(i, j):
    c = 1 # 이동 횟수
    Q = [(i, j)]
    while Q:
        i, j = Q.pop(0)
        for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            ni, nj = i+di, j+dj
            if 0 <= ni < N and 0 <= nj < N and arr[i][j] + 1 == arr[ni][nj]:
                Q.append((ni, nj))
                c += 1
    return c
# ------------------------------------------------------------
T = int(input())
for tc in range(1,1+T):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    max, num = 0, N+1
    for i in range(N):
        for j in range(N):
            cnt = f(i, j)
            if cnt == max:
                if arr[i][j] < num:
                    num = arr[i][j]
            elif cnt > max:
                max = cnt
                num = arr[i][j]
    print(f'#{tc} {num} {max}')