T = int(input())
for tc in range(1, 1+T):
    N = float(input())
    res = ''
    l = 0
    while N:
        N *= 2
        l += 1
        temp = str(N)
        res += temp[0]
        if temp[0] == '1':
            N -= 1
        if l == 13:
            res = 'overflow'
            break
    print(f'#{tc} {res}')
