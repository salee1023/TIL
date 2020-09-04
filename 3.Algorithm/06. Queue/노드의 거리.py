def f(s, g):
    Q = [s]
    visited = [0] * (V+1)
    visited[s] = 1
    # 출발지 정보 입력
    while Q:
        n = Q.pop(0)
        for i in range(1, V+1):  # 인접이고, enq되지 않은 노드
            if adj[n][i] == 1 and visited[i] == 0:
                Q.append(i)  # enq
                visited[i] = visited[n] + 1  # 방문 및 거리 표시
                if i == g:
                    return visited[i] - 1
    return 0
# ----------------------------------------
T = int(input())
for tc in range(1,1+T):
    V, E = map(int, input().split())
    adj = [[0]*(V+1) for _ in range(V+1)]
    for _ in range(E):
        i, j = map(int, input().split())
        adj[i][j] = 1
        adj[j][i] = 1
    S, G = map(int, input().split())
    print(f'#{tc} {f(S,G)}')
