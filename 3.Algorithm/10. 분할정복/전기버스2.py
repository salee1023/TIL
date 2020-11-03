def charge(n, k, c, e):
    global min
    if e < 0:
        return
    if c >= min:
        return
    if n == k:
        if c < min:
            min = c
        return

    charge(n+1, k, c+1, battery[n]-1) # n+1에서 교환
    charge(n+1, k, c, e-1) # n+1에서 교환 x

# --------------------------------------------
T = int(input())
for tc in range(1, 1+T):
    battery = list(map(int, input().split()))
    N = battery[0]
    min = 987654321
    charge(2, N, 0, battery[1]-1)
    print(f'#{tc} {min}')