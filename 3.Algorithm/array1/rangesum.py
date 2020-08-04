T = int(input())
for tc in range(1, T+1):
    N,M = map(int, input().split())
    arr = list(map(int, input().split()))

    min = max = sum(arr[0:M])
    for i in range(0, (N-M)+1):
        cp = sum(arr[i:i+M])
        if cp < min:
            min = cp
        if cp > max:
            max = cp
    print(f'#{tc} {max-min}')