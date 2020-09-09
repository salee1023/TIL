def is_increase(s):
    for i in range(len(s)-1):
        if s[i] > s[i+1]:
            return False
    else:
        return True
# ---------------------------------------
T = int(input())
for tc in range(1, 1+T):
    N = int(input())
    arr = list(map(int, input().split()))
    ans = []
    for i in range(N-1):
        for j in range(i+1, N):
            s = str(arr[i]*arr[j])
            if is_increase(s):
                ans.append(int(s))
    if ans: print(f'#{tc} {max(ans)}')
    else: print(f'#{tc} -1')
'''
1
4
2 4 7 10
'''