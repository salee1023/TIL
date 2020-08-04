T = int(input())
for tc in range(1,1+T):
    N = int(input())
    arr = list(map(int, input().split()))
    min = sum(arr)
    idx = 0

    for i in range(N):
        sub = abs(sum(arr[0:i]) - sum(arr[i:]))
        if sub < min:
            min = sub
            idx = i

    print(f'#{tc} {idx} {min}')