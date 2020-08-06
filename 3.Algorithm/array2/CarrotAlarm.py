T = int(input())
for tc in range(1,1+T):
    N = int(input())
    carrot = [list(int, input().split()) for _ in range(10)]
    cnt = 0
    # 경보기 위치 파악하기
    for i in range(10):
        for j in range(10):
            # 첫번째 모서리
            if carrot[i][j] == 0 and carrot[i][j+1] == 1 and carrot[i+1][j] == 1:
                for x in range(0, i+1):
                    for y in range(0, j+2):
                        if carrot[x][y] == 2:
                            cnt += 1
            # 두번째 모서리
            if carrot[i][j] == 1 and carrot[i][j+1] == 0 and carrot[i+1][j] == 1:
                for x in range(0, i+1):
                    for y in range(j+1, 10):
                        if carrot[x][y] == 2:
                            cnt += 1
            # 세번째 모서리
            if carrot[i][j] == 0 and carrot[i][j+1] == 1 and carrot[i+1][j] == 0:
                for x in range(0, i+2):
                    for y in range(0, j+1):
                        if carrot[x][y] == 2:
                            cnt += 1







