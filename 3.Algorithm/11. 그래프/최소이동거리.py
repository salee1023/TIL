def find(s):
    d = [x for x in adj[s]]  # 출발로부터의 거리
    u = [0] * (N+1)  # w로 선택여부 (거리 확정)
    cnt = 0

    while cnt < (N+1):  # 모든 노드가 w로 선택될 때 까지
        cnt += 1
        minV = INF
        w = 0
        for i in range(N+1):  # u[w] == 0을 만족하고, d[w]가 최소인 w 찾기
            if d[i] < minV and u[i] == 0:
                w = i
                minV = d[i]
        u[w] = 1
        for v in range(N+1):
            if 0 < adj[w][v] < INF and u[v] == 0:
                d[v] = min(d[v], d[w] + adj[w][v])
    return d[-1]

# ------------------------------------------
INF = 1000000000
T = int(input())
for tc in range(1, 1+T):
    N, E = map(int, input().split())
    adj = [[INF] * (N+1) for _ in range(N+1)]

    for i in range(N+1):
        adj[i][i] = 0

    for _ in range(E):
        n1, n2, d = map(int, input().split())
        adj[n1][n2] = d

    print(f'#{tc} {find(0)}')