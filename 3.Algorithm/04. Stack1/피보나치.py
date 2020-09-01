# 재귀
def fibo(n):
    if n < 2: # 기본 파트
        return n
    else:     # 유도 파트
        return fibo(n-1) + fibo(n-2)

print(fibo(8))   

# memoization
'''
def fibo2(n):
    if n >= 2 and len(memo) <= n:
        memo.append(fibo2(n-1) + fibo2(n-2))
    return memo[n]

memo = [0, 1] # 참조형은 global 안써도 된다.  값형은 read만 된다.
print(fibo2(7))
'''

# 반복
'''
def fibo3(n):
    f = [0, 1]
    for i in range(2, n+1):
        f.append(f[i-1] + f[i-2])
    return f[n]

print(fibo3(7))
'''