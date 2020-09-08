# 연결된 노드인지 확인하고 visited 체크 (bfs)
def group(s):
    Q = [s]
    v[s] = 1
    while Q:
        n = Q.pop(0)
        for i in range(1, N + 1):
            if adj[n][i] == 1 and v[i] == 0:
                Q.append(i)
                v[i] = 1

# ------------------------------------------------------------
T = int(input())
for tc in range(1,1+T):
    N, M = map(int, input().split()) # N:사람 수 M: 서로 알고있는 관계 수
    adj = [[0]*(N+1) for _ in range(N+1)]
    v = [0]*(N+1)
    c = 0
    for _ in range(M):
        a, b = map(int, input().split())
        adj[a][b] = 1
        adj[b][a] = 1
    for idx in range(1, N + 1):
        if v[idx] == 0:
            group(idx)
            c += 1
    print(f'#{tc} {c}')