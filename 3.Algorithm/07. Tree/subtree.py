def sub(N):
    global cnt
    if N:
        cnt += 1
        sub(tree[N][0])
        sub(tree[N][1])
# -------------------------------------
T = int(input())
for tc in range(1, 1+T):
    E, N = map(int, input().split())
    arr = list(map(int, input().split()))
    tree = [[0]*3 for _ in range(E+2)]
    cnt = 0
    for i in range(E):
        p, c = arr[2*i], arr[2*i+1]
        if tree[p][0] == 0:
            tree[p][0] = c
        else:
            tree[p][1] = c
        tree[p][2] = p
    sub(N)
    print(f'#{tc} {cnt}')