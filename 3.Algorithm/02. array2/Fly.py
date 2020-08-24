T = int(input())
for tc in range(1,T+1):
    N, M = map(int,input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    result = 0
    for x in range(N):
        for y in range(N):
            if 0 <= x <= N-M and 0 <= y <= N-M: # 파리잡기가 가능한 범위
                total = 0
                for i in range(x, x+M):
                    for j in range(y, y+M):
                        total += arr[i][j]
                if total > result:
                    result = total
    print(f'#{tc} {result}')