T = int(input())
for tc in range(1,1+T):
    N = int(input())
    carrot = [list(map(int, input().split())) for _ in range(10)]
    alarm = []
    new
    # 경보기 위치
    for i in range(10):
        for j in range(10):
            if carrot[i][j] == 1:
                alarm.append(i)
                alarm.append(j)
    alarm1 = alarm[0:2]
    alarm2 = alarm[len(alarm)-2:]
    # 멧돼지 확인 1
    for i in range(0, alarm1[0]+1):
        for j in





