# 재귀
def dfs(v):
    # 방문체크
    visited[v] = 1
    print(v, end=' ')
    # v의 인접한 정점중에서 방문안한 정점을 재귀호출
    for w in range(1,V+1):
        if G[v][w] == 1 and visited[w] == 0:
            dfs(w)          
# --------------------------------------------
V, E = map(int, input().split()) # 정점, 간선
temp = list(map(int, input().split())) # 간선들
G = [[0]*(V+1) for _ in range(V+1)] # 인접 행렬
visited = [0]*(V+1) # 방문 체크

# 간선들을 인접행렬에 저장
for i in range(E):
    s, e = temp[2*i], temp[2*i+1]
    G[s][e] = 1
    G[e][s] = 1

dfs(1)

# 반복
'''
def dfs2(s,V): 
    # 초기화, 스택 생성, visitied[] 생성 및 초기화
    visited = [0]*(V+1)
    stack = []
    stack.append(s) # 시작 노드 push()
    visited[s] = 1
    while stack: # 스택이 비어있지 않으면 반복
        n = stack.pop() # 탐색할 노드 선택
        for i in range(1,V+1):
            if adj[n][i] == 1 and visited[i] == 0: # n에 인접한 노드가 있고, 방문안한 노드일 때,
                stack.append(i)
                visited[i] = 1  
# --------------------------------------------------
V, E = map(int, input().split()) # V 정점 개수, E 간선 개수
adj = [[0]*(V+1) for _ in range(V+1)]
tmp = list(map(int, input().split()))
for i in range(E):
    n1, n2 = tmp[i*2], tmp[i*2+1]
    adj[n1][n2] = 1
    adj[n2][n1] = 1 # 무방향 그래프인 경우
dfs(1, V)                
'''

