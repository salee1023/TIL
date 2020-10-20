def cheese(N, M): # 다 녹으면 0, 치즈가 남아있으면 cnt
    cnt = 0
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 1:
                cnt += 1
    cheese_status.append(cnt)
    return cnt


def air(N, M):
    q = []
    q.append((0, 0))
    arr[0][0] = 2
    while q: # 큐가 비어있지 않으면
        i, j = q.pop()
        for k in range(4):
            ni, nj = i + di[k], j + dj[k]
            if 0 <= ni < N and 0 <= nj < M:
                if arr[ni][nj] == 0:
                    q.append((ni, nj))
                    arr[ni][nj] = 2


def melting(N, M):
    cnt = 0
    for i in range(1, N-1):
        for j in range(1, M-1):
            if arr[i][j] == 1: # 치즈이고 인접칸에 공기가 있으면
                for k in range(4):
                    ni, nj = i + di[k], j + dj[k]
                    if arr[ni][nj] == 2:
                        arr[i][j] = 0 # 치즈가 녹음

# ---------------------------------------------------------
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
v = [[0]*M for _ in range(N)] # 공기인 칸
cheese_status = [] # 치즈 녹는 현황

while cheese(N, M):
    air(N, M)
    melting(N, M)
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 2:
                arr[i][j] = 0

print(len(cheese_status)-1)
print(cheese_status[-2])








