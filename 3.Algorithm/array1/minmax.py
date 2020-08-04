T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    min = max = arr[0]
    for num in arr:
        if num < min:
            min = num
        elif num > max:
            max = num
    print(f'#{tc} {max-min}')

