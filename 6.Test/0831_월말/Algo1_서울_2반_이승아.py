# 배열 채우는 함수
def makearr(arr, M, D):
    # 우, 하, 좌, 상
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    # 중앙에 M 입력
    center = N // 2
    arr[center][center] = M

    # 4 방향으로 돌며 값 채우기
    for c in range(1,center+1): # c : center로 부터 떨어진 거리
        M += D # 입력할 값
        startx, starty = center-c, center-c # center의 좌측상단 대각선 꼭지점

        # 좌측상단 대각선 지점에서 시작해서 c*2 칸 만큼 값을 채우고, 4 방향으로 돌며 값을 채운다.
        for i in range(4):
            for d in range(c*2):
                arr[startx][starty] = M
                startx += dx[i]
                starty += dy[i]

# ----------------------------------------------------------------
T = int(input())
for tc in range(1,1+T):
    # N: 배열의 크기 M: 첫번째 입력 값 D: 변경 값
    N, M, D = map(int, input().split())
    # 크기가 N X N 이차원 배열 생성
    arr = list([0]*N for _ in range(N))
    # 배열 채우기
    makearr(arr, M, D)
    # 행의 합 출력하기
    print(f'#{tc} ', end='')
    for a in arr:
        print(f'{sum(a)} ', end='')
    print()

'''
3
7 5 2
9 10 -3
9 100 100
'''