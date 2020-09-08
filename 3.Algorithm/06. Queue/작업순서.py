def f(s):
    Q = [s]
    v[s] = 1
    while Q:
        n = Q.pop(0)
        route.append(n)
        for i in range(1, V+1): # 인접한 노드가 있으면
            if adj[n][i] == 1 and v[i] != 1: # 선행작업이 모두 완료된 노드인지 확인한다
                for j in range(1, V+1):
                    if check[i][j] == 1 and v[j] == 0: # 선행작업이 완료되지 않았으면 break
                        break
                else: # 선행작업이 모두 완료된 노드면 enq, 방문체크
                    Q.append(i)
                    v[i] = 1
# --------------------------------------
for tc in range(1,11):
    V, E = map(int, input().split())
    a = list(map(int, input().split()))
    start, route = [], []
    v = [0]*(V+1)
    # 인접행렬
    adj = [[0] * (V + 1) for _ in range(V + 1)]
    for i in range(0, E*2, 2):
        adj[a[i]][a[i+1]] = 1
    # 선행관계를 쉽게 파악하기 위한 전치행렬
    check = [[adj[i][j] for i in range(V+1)] for j in range(V+1)]
    # 선행작업이 필요 없는 노드부터 시작
    for i in range(1, 1 + V):
        if check[i].count(1) == 0:
            f(i)
    ans = ' '.join(map(str, route))
    print(f'#{tc} {ans}')



