T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    min = max = arr[0] + arr[1]
    for i in range(N-1):
        num = arr[i] + arr[i+1]
        if num < min:
            min = num
        elif num> max:
            max = num

    print(f'#{tc} {max} {min}')

