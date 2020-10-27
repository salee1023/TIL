T = int(input())
for tc in range(1, 1+T):
    N = int(input())
    arr = input()
    tmp = ''
    for a in arr:
        tmp += format(int(a, 16), '04b')

    print(f'#{tc} ', end='')
    for i in range(len(tmp)//7):
        print(int(tmp[7*i:7*i+7],2), end=' ')
    print()