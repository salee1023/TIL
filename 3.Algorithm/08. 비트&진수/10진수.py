T = int(input())
for tc in range(1, 1+T):
    arr = input()
    cut = []
    for i in range(len(arr)//7):
        cut.append(arr[i*7:i*7+7])
        i += 7
    print(f'#{tc}', end=' ')
    for c in cut:
        res = 0
        for i in range(7):
            res += int(c[i])*2**(6-i)
        print(f'{res}', end=' ')
    print()

