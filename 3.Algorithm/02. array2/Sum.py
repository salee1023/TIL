for tc in range(10):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]

    result = 0
    for i in range(100):
        row = col = dia = diar = 0
        for j in range(100):
            row += arr[i][j]
            col += arr[j][i]
            if i == j:
                dia += arr[i][j]
            if i+j == 99:
                diar += arr[i][j]
        if max(row, col, dia, diar) > result:
            result = max(row, col, dia, diar)

    print(f'#{N} {result}')