def find_f(n):
    q = [n]
    visited[n] = 1
    while q:
        x = q.pop(0)
        for i in rel[x]:
            if visited[i] == 0:
                q.append(i)
                visited[i] = visited[x] + 1

# --------------------------------------------
T = int(input())
for tc in range(1, 1+T):
    N, M = map(int, input().split())
    rel = [[] for _ in range(N + 1)]
    visited = [0] * (N + 1)
    for _ in range(M):
        a, b = map(int, input().split())
        rel[a].append(b)
        rel[b].append(a)
    find_f(1)
    print(f'#{tc} {visited.count(2) + visited.count(3)}')