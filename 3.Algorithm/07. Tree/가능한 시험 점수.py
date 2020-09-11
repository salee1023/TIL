T = int(input())
for tc in range(1, 1+T):
    N = int(input())
    S = [0]+list(map(int, input().split()))
    d = [[1]+[0]*(sum(S)) for _ in range(N+1)]
    for i in range(1, N+1):
        for j in range(1, sum(S)+1):
            if j >= S[i]:
                d[i][j] = d[i-1][j] or d[i-1][j-S[i]]
            else:
                d[i][j] = d[i-1][j]
    print(f'#{tc} {d[N].count(1)}')

