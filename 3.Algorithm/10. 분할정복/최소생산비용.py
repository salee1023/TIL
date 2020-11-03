def p(depth, n, res):
    global min

    if res >= min:
        return

    if depth == n:
        if res < min:
            min = res
        return

    else:
        for i in range(depth, n):
            factory[i], factory[depth] = factory[depth], factory[i]
            # 자리 정해지면 비용 계산
            p(depth+1, n, res+cost[depth][factory[depth]])
            factory[i], factory[depth] = factory[depth], factory[i]

# ------------------------------------------
T = int(input())
for tc in range(1, 1+T):
    N = int(input())
    cost = [list(map(int, input().split())) for _ in range(N)]
    min = 987654321
    factory = [i for i in range(N)]
    p(0, N, 0)
    print(f'#{tc} {min}')