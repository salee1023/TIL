def start(maze):
    for i in range(N):
        for j in range(N):
            if maze[i][j] == '2':
                return i, j


def f(i, j):
    global res
    visited = [[0] * N for _ in range(N)]
    distance = [[0] * N for _ in range(N)]
    Q = []
    # 출발지 정보 입력
    Q.append((i, j))
    visited[i][j] = 1
    distance[i][j] = 1
    while Q: #
        i, j = Q.pop(0)
        for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            ni, nj = i+di, j+dj
            if 0 <= ni < N and 0 <= nj < N and maze[ni][nj] != '1' and visited[ni][nj] == 0:
                Q.append((ni, nj))
                visited[ni][nj] = 1 # 방문체크
                distance[ni][nj] = distance[i][j] + 1 # 이전 지점까지의 거리 + 1
                if maze[ni][nj] == '3': # 도착
                    res =  distance[i][j] -1
# ----------------------------------------
T = int(input())
for tc in range(1,1+T):
    N = int(input())
    maze = [input() for _ in range(N)]
    res = 0
    si, sj = start(maze)
    f(si, sj)
    print(f'#{tc} {res}')