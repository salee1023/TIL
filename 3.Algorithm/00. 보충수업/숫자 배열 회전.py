T = int(input())
for tc in range(1, 1+T):
    N = int(input())
    arr = [input().split() for _ in range(N)]
    r90 = []
    r180 = []
    r270 = []

    for i in range(N):
        tmp = []
        for j in range(N):
            tmp.append(arr[j][i])
        tmp.reverse()
        r90.append(tmp)

    for i in range(N-1, -1, -1):
        tmp = []
        for j in range(N):
            tmp.append(arr[i][j])
        tmp.reverse()
        r180.append(tmp)

    for i in range(N-1, -1, -1):
        tmp = []
        for j in range(N):
            tmp.append(arr[j][i])
        r270.append(tmp)

    print(f'#{tc}')
    for i in range(N):
        print(''.join(r90[i]) + ' ' + ''.join(r180[i]) + ' ' + ''.join(r270[i]))

