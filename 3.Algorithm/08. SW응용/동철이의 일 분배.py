def p(n, k, x):
    global max
    if x <= max:
        return
    elif n == k and x > max:
        max = x
    else:
        for idx in range(n, k):
            arr[idx], arr[n] = arr[n], arr[idx]
            p(n+1, k, x*prob[n][arr[n]]/100)
            arr[idx], arr[n] = arr[n], arr[idx]

#--------------------------------------------------
T = int(input())
for tc in range(1, 1+T):
    N = int(input())
    prob = [list(map(int, input().split())) for _ in range(N)]
    arr = [i for i in range(N)]
    max = 0
    p(0, N, 1)
    print('#%d %.6f' % (tc, max*100))
