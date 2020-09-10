def make_t(n):
    global count
    if n <= N:
        make_t(n*2) # left
        tree[n] = count
        count += 1
        make_t(n*2+1) # right
# ------------------------
T = int(input())
for tc in range(1,1+T):
    N = int(input())
    tree = [0]*(N+1)
    count = 1
    make_t(1)
    print(f'#{tc} {tree[1]} {tree[N//2]}')