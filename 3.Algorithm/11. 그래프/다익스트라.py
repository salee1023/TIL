V, E = map(int, input().split())
INF = 1000000000
adj = [[INF]*V for _ in range(V)]

for i in range(V): # 자기 자신인 경우
    adj[i][i] = 0

# 인접행렬 생성
for _ in range(E):
    n1, n2, w = map(int, input().split())
    adj[n1][n2] = w

s = 0 # 시작 정점 번호
d = [x for x in adj[s]] # 출발로부터의 거리
u = [0]*V # w로 선택여부 (거리 확정)
cnt = 0

while cnt < V: # 모든 노드가 w로 선택될 때 까지
    cnt += 1
    minV = INF
    w = 0
    for i in range(V): # u[w] == 0을 만족하고, d[w]가 최소인 w 찾기
        if d[i] < minV and u[i] == 0:
            w = i
            minV = d[i]
    u[w] = 1
    for v in range(V):
        if 0 < adj[w][v] < INF and u[v] == 0:
            d[v] = min(d[v], d[w]+adj[w][v])
print(d)

'''
6 10
0 1 3
0 2 4
2 1 1
1 3 5
2 3 4
2 4 5
4 0 3
3 5 4
4 5 5
3 4 3
'''