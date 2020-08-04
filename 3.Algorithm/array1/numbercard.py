T = int(input())
for tc in range(1,T+1):
    N = int(input())
    numbers = input()
    countarr = [0]*10

    # 숫자가 몇 개 씩 있는지 배열 생성
    for i in range(N):
        countarr[int(numbers[i])] += 1

    max = countarr[0]
    idx = 0
    for i, val in enumerate(countarr):
        if val >= max:
            idx, max = i, val

    print(f'#{tc} {idx} {max}')