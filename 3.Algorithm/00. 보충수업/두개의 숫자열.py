def max_f(S,L):
    max_s = 0
    for i in range(len(L)-len(S)+1):
        arr = L[i:i+len(S)]
        sum = 0
        for j in range(len(S)):
            sum += S[j]*arr[j]
        if sum > max_s:
            max_s = sum
    return max_s
# -----------------------------------
T = int(input())
for tc in range(1,1+T):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    if N < M:
        print(f'#{tc} {max_f(A, B)}')
    else:
        print(f'#{tc} {max_f(B, A)}')
