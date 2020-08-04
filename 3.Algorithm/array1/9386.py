T = int(input())
for tc in range(1, T+1):
    N = int(input())
    num = input()
    newnum = []
    newnum.extend(num.split('0'))
    max = 0
    for one in newnum:
        count = one.count('1')
        if count> max:
            max = count
    print(f'#{tc} {max}')
