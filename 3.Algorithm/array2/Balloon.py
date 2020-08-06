T = int(input())
for tc in range(1, 1 + T):
    N, M = map(int, input().split())
    arr = [[0] * M for _ in range(N)]
    for i in range(N):
        arr[i] = list(map(int, input().split()))

    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    result = 0

    for x in range(N):
        for y in range(M):
            balloon = arr[x][y]
            for i in range(4):
                tx = x
                ty = y
                for _ in range(arr[x][y]): # 꽃가루 개수 만큼 터트린다
                    nx = tx + dx[i]
                    ny = ty + dy[i]
                    if 0 <= nx < N and 0 <= ny < M:
                        balloon += arr[nx][ny]
                        tx = nx
                        ty = ny
            if balloon > result:
                result = balloon

    print(f'#{tc} {result}')