def fibo(n):
    if n < 2: # 기본 파트
        return n
    else:     # 유도 파트
        return fibo(n-1) + fibo(n-2)

print(fibo(8))    