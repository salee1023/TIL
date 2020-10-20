def start(maze):
    for i in range(N):
        for j in range(N):
            if maze[i][j] == '2':
                return i, j

def f(i, j, N):
    if maze[i][j] =='3':
        return 1
    else:
        v[i][j] = 1
        # 인접(미로를 벗어나지 않고 벽이 아니면)하고 방문하지 않은 칸이면 이동
        for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            ni, nj = i+di, j+dj
            if 0 <= ni < N and 0 <= nj < N  and maze[ni][nj] != '1' and v[ni][nj] == 0:
                if f(ni, nj, N):
                    return 1
        return 0
# -----------------------------------------------
T = int(input())
for tc in range(1,1+T):
    N = int(input())
    maze = [input() for _ in range(N)]
    v = [[0]*N for _ in range(N)]
    starti, startj = start(maze) # 출발지
    print(f'#{tc} {f(starti, startj, N)}')

