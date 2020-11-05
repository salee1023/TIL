def p(depth, n, distance):
    global min

    if depth == n:
        if distance < min:
            min = distance
        return
    else:
        for i in range(depth, n):
            customer[i], customer[depth] = customer[depth], customer[i]
            # 자리 정해지면 비용 계산
            p(depth+1, n, res+cost[depth][customer[depth]])
            customer[i], customer[depth] = customer[depth], customer[i]

# -----------------------------------------
T = int(input())
for tc in range(1, 1+T):
    N = int(input())
    location = list(map(int, input().split()))
    min = 987654321
    customer = [i for i in range(N)]
    p(0, N, 0)
