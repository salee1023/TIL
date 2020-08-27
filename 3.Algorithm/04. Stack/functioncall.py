def f(n,k): # n 복사할 인덱스, k 배열의 크기
    if n == k: # 복사할 인덱스가 크기와 같으면 복사 완료
        print(A)
    else:
        A[n] = n+1
        f(n+1, k)


A = [0]*10
f(0,10)