T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [0]*N
    for i in range(N):
        arr[i] = list(map(int, input().split()))

    # 델타를 이용한 상하좌우
    dx = [0,0,-1,1]
    dy = [-1,1,0,0]

    result = 0
    for x in range(N):
        for y in range(N):
            for i in range(4):
                nx = x + dx[i] # 0
                ny = y + dy[i] # -1
                if  0 <= nx < N and 0 <= ny < N:
                    result += abs(arr[x][y] - arr[nx][ny])
    print(f'#{tc} {result}')