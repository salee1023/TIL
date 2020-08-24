T = int(input())
for tc in range(1,1+T):
    arr = list(map(int, input().split()))
    sub = ans = 0
    for i in range(1,1<<10): # 부분집합의 개수(공집합 제외)
        for j in range(10): # arr의 원소의 수만큼 비트를 교환
            if i & (1<<j):
                sub += arr[j]
        if sub == 0:
            ans = 1
            break
        else:
             sub = 0
    print(f'#{tc} {ans}')