def rotate(c, X, Y, K, N):
    # 회전 각도가 0이면 아무것도 return 하지 않는다.
    if c == 0:
        return
    else:
        mini_arr = [] # 부분 배열
        # 부분 배열 90도 회전하기
        if c == 90:
            for x in range(X-1, X+K-1):
                tmp = []
                for y in range(Y-1, Y+K-1):
                    tmp.append(arr[y][x])
                tmp.reverse()
                mini_arr.extend(tmp)
        # 부분 배열 180도 회전하기
        elif c == 180:
            for y in range(Y+K-2, Y-2, -1):
                tmp = []
                for x in range(X-1, X+K-1):
                    tmp.append(arr[y][x])
                tmp.reverse()
                mini_arr.extend(tmp)
        # 부분 배열 270도 회전하기
        else:
            for x in range(X+K-2, X-2, -1):
                tmp = []
                for y in range(Y-1, Y+K-1):
                    tmp.append(arr[y][x])
                mini_arr.extend(tmp)
        # 회전시킨 부분 배열을 원래 배열로 update
        i = 0
        for y in range(Y-1, Y+K-1):
            for x in range(X-1, X+K-1):
                arr[y][x] = mini_arr[i]
                i += 1


#-------------------------------------------------------------------------------
T = int(input())
for tc in range(1, 1+T):
    # N: 배열의 크기, C: 회전 각도, (X,Y): 시작 위치, K: 부분 영역 가로세로 값, R: 출력 행
    N, C, X, Y, K, R = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 부분 사각형이 시작 위치를 기준으로 N X N 영역을 벗어나는 지 확인한다.
    # 시작 좌표에서 K만큼 이동한 좌표가 배열의 크기 N을 넘어가면 -1을 출력한다.
    if X+K-1 > N or Y+K-1 > N:
        print(f'#{tc} -1')
    # 부분 사각형이 배열 안에 온전히 존재하면 부분 사각형을 회전시킨다.
    else:
        # 360도 회전하면 처음과 같기 때문에 C를 360으로 나눈 나머지 만큼 회전시키면 된다.
        rotate(C % 360, X, Y, K, N)
        # 회전을 완료한 배열의 R번째 행의 합을 출력한다.
        print(f'#{tc} {sum(arr[R-1])}')
