T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    max_c = 0
    for i in range(N):
        c = 0
        for j in range(i+1,N):
            if arr[i] > arr[j]:
                c += 1
        if max_c < c:
            max_c = c
    print(f'#{tc} {max_c}')