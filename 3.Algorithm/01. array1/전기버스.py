T = int(input())
for tc in range(1, T+1):
    K, N, M = map(int, input().split())
    # 충전소
    charger = list(map(int, input().split()))

    last = 0
    cnt = 0
    while last+ K < N: # 종점에 도착하지 않았으면
        for i in range(K,0,-1): # 한번에 갈 수 있는 거리에 충전소가 있을 때
            if (last + i) in charger:
                cnt += 1
                last += i
                break
        else: # 한번에 갈 수 있는 거리에 충전소가 없을 때
            print(f'#{tc} 0')
            break
    else: # 종점 도착
        print(f'#{tc} {cnt}')