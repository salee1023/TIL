def make_t():
    for i in range(N-M, 0, -1):
        if i*2 == N:
            tree[i] = tree[i*2]
        else:
            tree[i] = tree[i*2] + tree[i*2 + 1]
# -------------------------------------
T = int(input())
for tc in range(1,1+T):
    N, M, L = map(int, input().split())
    tree = [0]*(N+1)
    for _ in range(M):
        n, v = map(int, input().split())
        tree[n] = v
    make_t()
    print(f'#{tc} {tree[L]}')