def f(M, C):
    # 자석 회전 유무, 방향 찾기
    idx = [0, 0, 0, 0]
    idx[M-1] -= C
    cnt = 0
    for m in range(M, 1, -1):
        cnt += 1
        if magnet[m-1][6] != magnet[m-2][2]:
            if cnt % 2:
                idx[m-2] += C
            else:
                idx[m-2] -= C
        else:
            break
    cnt = 0
    for m in range(M, 4):
        cnt += 1
        if magnet[m-1][2] != magnet[m][6]:
            if cnt % 2:
                idx[m] += C
            else:
                idx[m] -= C
        else:
            break

    # 실제 자석 회전시키기
    for i in range(4):
        if idx[i] == -1:
            tmp = magnet[i][7]
            for j in range(7, 0, -1):
                magnet[i][j] = magnet[i][j-1]
            magnet[i][0] = tmp

        if idx[i] == 1:
            tmp = magnet[i][0]
            for j in range(7):
                magnet[i][j] = magnet[i][j+1]
            magnet[i][7] = tmp
# ----------------------------------------------------------------
T = int(input())
for tc in range(1, 1+T):
    N = int(input())
    magnet = [list(map(int, input().split())) for _ in range(4)]

    for n in range(N):
        M, C = map(int, input().split())
        f(M, C)

    res = 0
    for n in range(4):
        res += (2**n)*magnet[n][0]
    print(f'#{tc} {res}')
