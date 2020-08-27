def fibo2(n):
    if n >= 2 and len(memo) <= n:
        memo.append(fibo2(n-1) + fibo2(n-2))
    return memo[n]

memo = [0, 1] # 참조형은 global 안써도 된다.  값형은 read만 된다.
print(fibo2(7))