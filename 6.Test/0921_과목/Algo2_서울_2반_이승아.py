T = int(input())
for tc in range(1, 1+T):
    N = int(input())
    R, C = map(int, input().split()) # (R,C): 처음 폭탄 폭발 지점
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0]*N for _ in range(N)] # 폭탄 지점 방문 여부
    # 델타 이동
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    # 폭탄의 총 수
    res = 0
    # 처음 지점에 폭탄이 없을 때
    if arr[R][C] == 0:
        print(f'#{tc} 0')
    # 처음 지점에 폭탄이 있을 때
    else:
        # 처음 위치 push, 방문 체크
        stack = []
        stack.append((R, C))
        visited[R][C] = 1
        # 모든 폭탄을 터뜨릴 때 까지 반복
        while stack:
            R, C = stack.pop()
            res += 1 # 폭탄 터뜨리고 res + 1
            bomb = arr[R][C] # 폭발력
            for d in range(4):
                x, y = R, C
                for b in range(bomb):
                    nx, ny = x+dx[d], y+dy[d]
                    # NxN 범위를 벗어나지 않고, 폭탄이 있고, 방문하지 않은 지점일 때
                    if 0 <= nx < N and 0 <= ny < N and arr[nx][ny] > 0 and visited[nx][ny] == 0:
                        # 폭탄 위치 push, 방문체크
                        stack.append((nx, ny))
                        visited[nx][ny] = 1
                    x, y = nx, ny
        print(f'#{tc} {res}')

# Test case
'''
3
4 
3 3
0 0 1 0
0 2 0 1
0 0 0 0
1 1 0 2
6
3 2
0 0 0 0 0 0
0 0 3 0 1 1
1 0 0 0 0 0
0 0 3 0 0 2
2 0 0 0 0 0
0 1 0 2 0 2
10 
8 7
0 3 0 0 3 0 0 0 0 0
0 3 0 0 0 0 0 1 0 3
0 0 5 0 0 0 0 0 3 0
0 0 0 0 0 0 0 0 0 0 
0 5 0 0 0 2 0 5 0 0
0 0 0 0 0 3 0 2 0 4
4 0 2 0 0 2 1 4 0 0
0 0 0 0 0 5 0 0 0 0
0 0 0 0 0 0 4 5 5 1
3 0 3 0 2 4 0 0 0 1
'''