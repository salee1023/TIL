for tc in range(1,11):
    N = int(input())
    arr = list(map(int, input().split()))
    total = 0
    for i in range(2,N-2):
        if arr[i] == max(arr[i-2:i+3]):
            total += arr[i] - (max(arr[i-2], arr[i-1], arr[i+1], arr[i+2]))
    print(f'#{tc} {total}')