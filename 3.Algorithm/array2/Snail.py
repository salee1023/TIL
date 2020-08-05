T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [[0]*N for _ in range(N)]

    # RDLU
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    x = y = i = 0
    for num in range(1, N**2+1): # 숫자범위
        # 방향이 바뀌어야하는 지점
        if x < 0 or y < 0 or x > N-1 or y > N-1 or arr[x][y] != 0:
            # 한 칸 back
            x -= dx[i]
            y -= dy[i]
            # 방향 변경
            i = (i+1) % 4
            # 이동
            x += dx[i]
            y += dy[i]
        # 숫자 넣고 이동
        arr[x][y] = num
        x += dx[i]
        y += dy[i]

    # 출력
    print(f'#{tc}')
    for a in range(N):
        for b in range(N):
            print(arr[a][b] ,end=' ')
        print()