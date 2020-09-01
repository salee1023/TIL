def minsum(row, N, sum):
    global m
    # 모든 행을 검사했을 때
    if row == N:
        if sum < m:
            m = sum
    elif m <= sum:
        return
    else:
        for col in range(N):
            if visited[col] == 0:
                visited[col] = 1
                minsum(row+1, N, sum+arr[row][col])
                visited[col] = 0
# --------------------------------------
T = int(input())
for tc in range(1,1+T):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [0]*N # 방문한 열
    m = 10000000
    minsum(0,N,0)
    print(f'#{tc} {m}')