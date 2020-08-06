T = int(input())
for tc in range(1,1+T):
    N, M = map(int, input().split())
    carrot = [list(map(int, input().split())) for _ in range(N)]
    result = 987654321
    for i in range(N-1):
        for j in range(M-1):
            c = [0]*3
            # 1번 일꾼
            for x in range(i+1):
                for y in range(0, j+1):
                    c[0] += carrot[x][y]
            # 2번 일꾼
            for x in range(i+1):
                for y in range(j+1, M):
                    c[1] += carrot[x][y]
            # 3번 일꾼
            for x in range(i+1, N):
                for y in range(M):
                    c[2] += carrot[x][y]
            # 최소 차이
            diff = max(c)-min(c)
            if diff< result:
                result = diff
    print(f'#{tc} {result}')