T = int(input())
for tc in range(1,T+1):
    number = int(input())
    arr = [0]*12

    for i in range(6):
        arr[number%10] += 1
        number //= 10

    i = T = R = 0
    while i < 10:
        if arr[i] >= 3:
            T += 1
            arr[i] -= 3
            continue
        if arr[i] >= 1 and arr[i+1] >= 1 and arr[i+2] >= 1:
            R += 1
            arr[i] -= 1
            arr[i+1] -= 1
            arr[i+2] -= 1
            continue
        i += 1
    if T+R == 2:
        print(f'#{tc} Baby Gin')
    else:
        print(f'#{tc} Lose')
