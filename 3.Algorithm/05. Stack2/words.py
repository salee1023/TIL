def count(P,N,K):
    ans = 0
    for i in range(N):
        c = 0
        for j in range(N):
            if P[i][j]: 
                c += 1
            else: 
                if c == K: 
                    ans += 1
                    c = 0
                else:
                    c = 0
        if c == K:
            ans += 1            
    return ans        
# ------------------------------------
T = int(input())
for tc in range(1,1+T):
    N, K = map(int, input().split()) # N: 퍼즐크기, K: 단어 길이
    puzzle = [list(map(int, input().split())) for _ in range(N)]
    r_puzzle = [[puzzle[j][i] for j in range(N)] for i in range(N)]
    print(f'#{tc} {count(puzzle,N,K)+count(r_puzzle,N,K)}')