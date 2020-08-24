T = int(input())
for tc in range(1,1+T):
    N = int(input())
    carrot = [list(map(int, input().split())) for _ in range(10)]
    alarm = []
    # 경보기 위치
    for i in range(10):
        for j in range(10):
            if carrot[i][j] == 1:
                alarm.append(i)
                alarm.append(j)
    alarm1 = alarm[0:2] # 왼쪽위 좌표
    alarm2 = alarm[len(alarm)-2:] # 오른쪽아래 좌표
    # 멧돼지 감지
    cnt = 0
    for x in range(0, alarm1[0]+1): # 1
        for y in range(0, alarm1[1]+1):
            if carrot[x][y] == 2:
                cnt += 1
    for x in range(0, alarm1[0]+1): # 2
        for y in range(alarm2[1], 10):
            if carrot[x][y] == 2:
                cnt += 1
    for x in range(alarm2[0], 10): # 3
        for y in range(0, alarm1[1]+1):
            if carrot[x][y] == 2:
                cnt += 1
    for x in range(alarm2[0], 10): # 4
        for y in range(alarm2[1], 10):
            if carrot[x][y] == 2:
                cnt += 1

    print(f'#{tc} {cnt}')