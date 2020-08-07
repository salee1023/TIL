T = int(input())
for tc in range(1, 1+T):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    area = []
    # 구역 찾기
    for i in range(N):
        for j in range(N):
            if arr[i][j] != 0:
                r, c = i, j
                while r < N and arr[r][j] != 0:
                    r += 1
                while c < N and arr[i][c] != 0:
                    c += 1
                area.append([r-i, c-j])
                for x in range(i,r):
                    for y in range(j,c):
                        arr[x][y] = 0
    # 넓이 , 행 순으로 정렬하기
    area.sort(key= lambda x : [x[0]*x[1], x[0]])
    print(f'#{tc} {len(area)}', end =' ')
    for num in area:
        print(*num, end = ' ')
    print()
