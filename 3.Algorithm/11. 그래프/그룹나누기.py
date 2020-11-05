def find_set(x):
    if p[x] == x:
        return x
    else:
        return find_set(p[x])


def union(x, y):
    x = find_set(x)
    y = find_set(y)
    p[y] = x

# ------------------------------------------------
T = int(input())
for tc in range(1, 1+ T):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    p = [i for i in range(N+1)]
    cnt = 0

    for i in range(M):
        union(arr[2*i], arr[2*i+1])

    for i in range(1, 1+N):
        if p[i] == i:
            cnt += 1

    print(f'#{tc} {cnt}')