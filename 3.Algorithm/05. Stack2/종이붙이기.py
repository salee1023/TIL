def f(n):
    if n == 1: return 1
    if n == 2: return 3

    if memo[n]: return memo[n]
    
    memo[n] = f(n-1) + f(n-2)*2
    return memo[n]


for tc in range(1,int(input())+1):
    N = int(input()//10)
    memo = [0]*(N+1)
    print(f(N))
