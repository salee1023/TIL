def make_t(i):
    if tree[i]:
        return tree[i]
    else:
        if i*2 == N:
            return tree[i*2]
        else:
            return make_t(i*2) + make_t(i*2+1)
# -------------------------------------
T = int(input())
for tc in range(1,1+T):
    N, M, L = map(int, input().split())
    tree = [0]*(N+1)
    for _ in range(M):
        n, v = map(int, input().split())
        tree[n] = v
    print(f'#{tc} {make_t(L)}')