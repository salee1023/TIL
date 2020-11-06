# 방향 0, 1, 2, 3, 오른쪽부터 시계방향
# k 방향에 대해 마주보는 방향 (k+2)%4
def bfs(i, j, L):
    q = [] # 큐 생성
    q.append((i, j)) # 시작점 인큐
    v[i][j] = 1 # 1시간에 진입하는 위치
    cnt = 0
    while q:
        i, j = q.pop(0) # 탈주범이 머물렀던 위치
        cnt += 1 # 탈주범이 머물렀던 칸 수
        if v[i][j] < L: # L-1 시간에 갈 수 있는 칸이면
            for k in range(4): # 4 방향에 대해, 1시간 후 갈 수 있는 칸 확인
                di, dj = d[k]
                ni, nj = i+di, j+dj
                # 이웃칸 좌표가 유효하고, 아직 머무른 적이 없으면
                if 0 <= ni < N and 0 <= nj < M and v[ni][nj] == 0:
                    # 현재칸이 k 방향으로 열려있고, 이웃칸 (k+2)%4 방향이 열려있으면,
                    if tunnel[arr[i][j]][k] and tunnel[arr[ni][nj]][(k+2)%4]:
                        q.append((ni, nj))
                        v[ni][nj] = v[i][j] + 1

    return cnt # L시간까지 머물 수 있는 칸 수

# -----------------------------------------------
# 우하좌상
tunnel = [[0, 0, 0, 0],
          [1, 1, 1, 1],
          [0, 1, 0, 1],
          [1, 0, 1, 0],
          [1, 0, 0, 1],
          [1, 1, 0, 0],
          [0, 1, 1, 0],
          [0, 0, 1, 1]]

d = [(0, 1), (1, 0), (0, -1), (-1, 0)]
T = int(input())
for tc in range(1, 1+T):
    N, M, R, C, L = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    v = [[0]*M for _ in range(N)]

    r = bfs(R, C, L)
    print(f'#{tc} {r}')