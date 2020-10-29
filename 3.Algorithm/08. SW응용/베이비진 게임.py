def babygin():
    i = r1 = t1 = r2 = t2 = 0
    while i < 10:
        if (player1[i] >= 3) or (player1[i] >= 1 and player1[i+1] >= 1 and player1[i+2] >= 1):
            return 1
        if (player2[i] >= 3) or player2[i] >= 1 and player2[i+1] >= 1 and player2[i+2] >= 1:
            return 2
        i += 1
    return 0

#------------------------------------------------
T = int(input())
for tc in range(1, 1+T):
    player1 = [0]*12
    player2 = [0]*12
    arr = list(map(int, input().split()))
    i = v = 0
    #  player1, player2에게 카드를 한 장 씩 나누어주며 babygin 여부를 확인한다.
    while i < 12:
        if i % 2:
            player2[arr[i]] += 1
        else:
            player1[arr[i]] += 1

        if i >= 4:
            res = babygin()
            # player1, player2중에 누군가 이겼을 때
            if res:
                print(f'#{tc} {res}')
                v = 1
        if v == 1:
            break
        i += 1
    # 끝까지 무승부이면 0 출력
    if v == 0:
        print(f'#{tc} 0')
