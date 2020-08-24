T = int(input())
for tc in range(1, 1+T):
    N = int(input())
    arr = [0]*N
    for i in range(N):
        arr[i] = list(map(int, input().split()))

    # 각 영역의 총 개수를 저장
    carrots =[0]*4
    for i in range(N):
        for j in range(N):
            if i < j and i+j < N-1: # 1
                carrots[0] += arr[i][j]
            if i < j and i+j >= N: # 2
                carrots[1] += arr[i][j]
            if i > j and i+j >= N: # 3
                carrots[3] += arr[i][j]
            if i > j and i+j < N-1: # 4
                carrots[2] += arr[i][j]
    print(f'#{tc} {max(carrots)-min(carrots)}')
