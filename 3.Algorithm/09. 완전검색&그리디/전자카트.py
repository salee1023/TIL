def p(depth, n):
    if depth == n:
        route.append(arr[:])
        return
    for idx in range(depth, n):
        arr[idx], arr[depth] = arr[depth], arr[idx]
        p(depth+1, n)
        arr[idx], arr[depth] = arr[depth], arr[idx]

#----------------------------------------------------------------
T = int(input())
for tc in range(1, 1+T):
    N = int(input())
    battery = [list(map(int, input().split())) for _ in range(N)]
    arr = [n+2 for n in range(N-1)]
    route = []
    # 경로 경우의수 (순열)
    p(0, N-1)
    # 각 경로의 배터리 소비량 찾기
    min = 987654321
    res = 0
    while route:
        r = route.pop()
        res += battery[0][r[0]-1]
        for i in range(len(r)-1):
            res += battery[r[i]-1][r[i+1]-1]
        res += battery[r[-1]-1][0]
        if res < min:
            min = res
        res = 0
    print(f'#{tc} {min}')