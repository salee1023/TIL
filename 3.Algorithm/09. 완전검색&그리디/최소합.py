T = int(input())
for tc in range(1, 1+T):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    distance = [[0]*N for _ in range(N)]
    distance[0][0] = arr[0][0]
    for x in range(N):
        for y in range(N):
            if x == 0:
                distance[x][y] = distance[x][y-1] + arr[x][y]
            elif y == 0:
                distance[x][y] = distance[x-1][y] + arr[x][y]
            else:
                distance[x][y] = min(distance[x][y-1], distance[x-1][y]) + arr[x][y]
    print(f'#{tc} {distance[N-1][N-1]}')