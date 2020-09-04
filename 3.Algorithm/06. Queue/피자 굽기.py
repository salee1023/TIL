def cook(C):
    Q = []
    for i in range(N): # 오븐에 N개의 피자번호와 피자를 저장한다
        Q.append([i, C[i]])
    p_i = 0
    while len(Q) != 1: # 오븐에 피자가 1개 남을 때 까지
        pizza = Q.pop(0)
        if pizza[1] // 2 == 0: # 치즈가 다 녹으면
            if N + p_i < M: # 다음 순서 피자 넣기
                Q.append([N+p_i, C[N+p_i]])
                p_i += 1
        else:
            pizza[1] //= 2
            Q.append(pizza)
    else:
        last_pizza = Q.pop(0)
        return last_pizza[0]+1
# ----------------------------------------
T = int(input())
for tc in range(1,1+T):
    N, M = map(int, input().split())
    C = list(map(int, input().split()))
    print(f'#{tc} {cook(C)}')