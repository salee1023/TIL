def bfs(s,N): # 1~N번 노드가 존재하는 그래프 탐색
    q = [s] # 큐생성, 시작점 enq
    v = [0] * (N+1)
    v[s] = 1
    while q:
        t = q.pop(0) # deq
        # 여기서 t 노드에 디한 처리

        for i in range(1, N+1): # 인접이고, enq되지 않은 노드
            if adj[t][i] ==1 and v[i] == 0:
                q.append(i) # enq
                v[i] = v[t] + 1 # 방문표시 (거리를 표현해준다)