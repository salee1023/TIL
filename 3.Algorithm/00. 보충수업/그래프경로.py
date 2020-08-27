def f1(stx,  goal, V): # dfs반복
    stack = []
    stack.append(stx) # 시작점 push
    v = [0]*(V+1) # visited
    
    while stack: # 탐색할 노드가 있으면 반복
        n = stack.pop()
        if v[n] == 0: # 방문 안한 노드
            v[n] = 1
            if n == goal:
                return 1
            for i in range(1,V+1):
                if graph[n][i] == 1: # 방문한 적 없고 n에 인접한 노드
                    stack.append(i)                      
    return 0 # 다 돌았는데 목적지에 도착 못했을 때


T = int(input())
for tc in range(1,1+T):
    V, E = map(int, input().split())
    graph = [[0]*(V+1) for _ in range(V+1)]
    for e in range(E):
        i, j = map(int, input().split())
        graph[i][j] = 1 # 방향성 그래프
    S, G = map(int, input().split())
    print(f'#{tc} {f1(S,G,V)}') 
      