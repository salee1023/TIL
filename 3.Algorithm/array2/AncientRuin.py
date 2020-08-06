T = int(input())
for tc in range(1,1+T):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    result = 0
    for i in range(N):
        cnt = 0
        for j in range(M):
            if arr[i][j] == 1:
                cnt += 1
            elif cnt > result:
                result = cnt
                cnt = 0
            else:
                cnt = 0
        if cnt > result:
            result = cnt

    for j in range(M):
        cnt2 = 0
        for i in range(N):
            if arr[i][j] == 1:
                cnt2 += 1
            if cnt2 > result:
                result = cnt2
                cnt2 = 0
            else:
                cnt2 = 0
        if cnt2 > result:
            result = cnt2

    print(f'#{tc} {result}')