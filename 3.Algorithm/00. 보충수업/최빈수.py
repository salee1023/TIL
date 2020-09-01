T = int(input())
for tc in range(1, 1+T):
    N = int(input())
    count = [0]*101
    nums = list(map(int, input().split()))
    for i in range(1000):
        count[nums[i]] += 1
    max = 0
    ans = 0
    for c in range(1, 101):
        if count[c] >= max:
            max = count[c]
            ans = c
    print(f'#{tc} {ans}')
