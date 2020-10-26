def solution(n, s, a, b, fares):
    answer = 0
    min_f = 987654321
    adj = [[0]*(n+1) for _ in range(n+1)]
    visited = [0]*(n+1)
    for f in range(len(fares)):
        adj[fares[f][0]][fares[f][1]] = fares[f][2]
        adj[fares[f][1]][fares[f][0]] = fares[f][2]

    q = [s]
    visited[s] = 1
    while q:
        n = q.pop(0)
        for i in range(1, n+1):
            if adj[n][i] != 0:
                q.append(i)
                visited[i] += adj[n][i]
        if visited[a] != 0 and visited[b] != 0:
            break
    else:
        if max(visited[a], visited[b]) < min_f:
            min_f = max(visited[a], visited[b])
    print(visited)
    answer = min_f
    return answer

n, s, a, b = 6, 4, 6, 2
fares = [[4, 1, 10],
         [3, 5, 24],
         [5, 6, 2],
         [3, 1, 41],
         [5, 1, 24],
         [4, 6, 50],
         [2, 4, 66],
         [2, 3, 22],
         [1, 6, 25]]
print(solution(n, s, a, b, fares))