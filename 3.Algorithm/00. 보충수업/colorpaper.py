def paper(n):
    if n == 1: return 1
    elif n == 2: return 3
    else: return paper(n-1) + 2*paper(n-2)        
# -----------------------------------------
T = int(input())
for tc in range(1,1+T):
    N = int(input())
    print(f'#{tc} {paper(N//10)}')