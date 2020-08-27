'''
7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
'''
def dfs(v):
    # 방문체크
    visited[v] = 1
    print(v, end=' ')
    # v의 인접한 정점중에서 방문안한 정점을 재귀호출
    for w in range(1,V+1):
        if G[v][w] == 1 and visited[w] == 0:
            dfs(w)

# 정점, 간선
V, E = map(int, input().split())
# 간선들
temp = list(map(int, input().split()))
# 인접 행렬
G = [[0]*(V+1) for _ in range(V+1)]
# 방문 체크
visited = [0]*(V+1)

# 간선들을 인접행렬에 저장
for i in range(E):
    s, e = temp[2*i], temp[2*i+1]
    G[s][e] = 1
    G[e][s] = 1

dfs(1)
