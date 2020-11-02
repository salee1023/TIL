T = int(input())
for tc in range(1, 1+T):
    N = int(input())
    time_table = [list(map(int, input().split())) for _ in range(N)]
    time_table.sort(key=lambda x: x[1])
    i = res = tmp = 0
    while i < N:
        if time_table[i][0] >= tmp:
            res += 1
            tmp = time_table[i][1]
        i += 1
    print(f'#{tc} {res}')