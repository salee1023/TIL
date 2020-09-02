T = int(input())
for tc in range(1, 1+T):
    N = int(input())

    # 버스 노선
    A = [0]*(N+1)
    B = [0]*(N+1)
    for i in range(1,N+1):
        A[i], B[i] = map(int, input().split())

    # 정류장마다 몇개의 노선이 지나가는지 계산
    P = int(input())
    count = [0]*(P+1)
    for c in range(1,P+1):
        x = int(input())
        for j in range(1,N+1):
            if A[j] <= x <= B[j]:
                count[c] += 1

    # 출력
    print(f'#{tc} ', end='')
    for c in range(1, P+1):
        print(f'{count[c]} ', end='')
    print()