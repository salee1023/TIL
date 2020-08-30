def game(puzzle,i,j, s):
    dx = [-1, 0, 1, 1, 1, 0, -1, -1]
    dy = [-1, -1, -1, 0, 1, 1, 1, 0]
    for d in range(8):
        x = i + dx[d]
        y = j + dy[d]
        cnt = 0
        if puzzle[x][y] != 0 and puzzle[x][y] != s and puzzle[x + dx[d]][y + dy[d]] != 0: # 주변에 돌이 있고 색이 다르면
            while puzzle[x][y] != s: # 같은 색 돌이 나올 때 까지
                cnt += 1
                x += dx[d]
                y += dy[d]
                if puzzle[x][y] == 0:
                    cnt = 0
                    break
            x = i + dx[d]
            y = j + dy[d]
            while cnt > 0:
                puzzle[x][y] = s
                x += dx[d]
                y += dy[d]
                cnt -= 1
            x = i
            y = j
# ------------------------------------
T = int(input())
for tc in range(1,1+T):
    N, M = map(int, input().split())
    puzzle = [[0]*(N+2) for _ in range(N+2)]
    puzzle[N//2][N//2], puzzle[N//2][N//2+1], puzzle[N//2+1][N//2], puzzle[N//2+1][N//2+1] = 'W', 'B', 'B', 'W'
    for _ in range(M): # 돌을 넣을 때마다 확인
        i, j, s = map(int, input().split())
        if s == 1:
            puzzle[i][j] = 'B' # 1: 흑색
        else:
            puzzle[i][j] = 'W' # 2 -> -1 : 백색
        game(puzzle, i, j, puzzle[i][j])
    b = 0
    w = 0
    for i in puzzle:
        b += i.count('B')
        w += i.count('W')
    print(f'#{tc} {b} {w}')

