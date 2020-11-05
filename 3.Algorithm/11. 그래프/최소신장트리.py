def find_set(x):
    if p[x] == x:
        return x
    else:
        return find_set(p[x])


def union(x, y):
    x = find_set(x)
    y = find_set(y)
    if x > y:
        p[x] = y
    else:
        p[y] = x
    visited[x], visited[y] = 1, 1

# -----------------------------------------
T = int(input())
for tc in range(1, 1+T):
    V, E = map(int, input().split())
    edge = [list(map(int, input().split())) for _ in range(E)]
    edge.sort(key=lambda x: -x[2])
    p = [i for i in range(V+1)]
    visited = [0]*(V+1)
    res = 0

    while edge:
        a, b, w = edge.pop()
        if find_set(a) != find_set(b):
            union(a, b)
            res += w
        if visited.count(0) == 0:
            break

    print(f'#{tc} {res}')
