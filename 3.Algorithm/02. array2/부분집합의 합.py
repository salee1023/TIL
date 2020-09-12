T = int(input())
for tc in range(1,1+T):
    N, K = map(int, input().split())
    arr = [n+1 for n in range(12)]
    result = 0
    for i in range(1, 1 << 12): #부분집합의 개수
        sub = cnt = 0
        for j in range(12):
            if i & (1 << j):
                sub += arr[j]
                cnt += 1
        if sub == K and cnt == N:
            result += 1
    print(f'#{tc} {result}')