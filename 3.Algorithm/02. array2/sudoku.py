T = int(input())
for tc in range(1,1+T):
    puzzle = [list(map(int, input().split())) for _ in range(9)]
    result = 1
    # 행/열
    for i in range(9):
        row = [0] * 9
        col = [0] * 9
        for j in range(9):
            row[puzzle[i][j]-1] += 1
            col[puzzle[j][i]-1] += 1
        if row.count(1) < 9 or col.count(1) < 9:
            result = 0
            break
    # 3 x 3
    for i in range(0,9,3):
        for j in range(0,9,3):
            box = [0] * 9
            for x in range(i, i+3):
                for y in range(j, j+3):
                    box[puzzle[x][y]-1] += 1
            if box.count(1) < 9:
                result = 0
                break

    print(f'#{tc} {result}')