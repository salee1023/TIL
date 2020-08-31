# 필요한 물고기 수 찾는 함수
def countfish(arr, N, M):
    fish = 0
    for i in range(N):
        for j in range(M):
            # 연못이 하나라도 있으면 물고기 +1
            if arr[i][j] == 1: # 기준 연못 위치
                fish += 1
                r, c = i, j

                # 기준 연못에서 오른쪽으로 이어진 연못 파악하기 (행)
                while c < M and arr[i][c] != 0:
                    c += 1

                # 위의 행 범위 내에서 아래로 이어진 연못 파악하기 (열)
                for x1 in range(j, c):
                    while r < N and arr[r][x1] != 0:
                        r += 1
                    # 아래 방향까지 인접한 지 파악이 완료된 연못은 0으로 없애준다
                    for x2 in range(i, r+1):
                        arr[x2][x1] = 0
    return fish

# --------------------------------------------------
T = int(input())
for tc in range(1, 1+T):
    # M: 마당 가로 길이 N: 마당 세로 길이 K: 연못 좌표 개수
    M, N, K = map(int, input().split())
    # 마당 (countfish함수의 indexerror를 대비하여, N+1로 행을 하나 늘려준다)
    arr = list([0]*M for _ in range(N+1))

    # 연못 위치 파악
    for _ in range(K):
        i, j = map(int, input().split())
        arr[j][i] = 1

    # 필요한 물고기 수 출력하기
    print(f'#{tc} {countfish(arr, N, M)}')

'''
3
10 8 17
0 0
1 0
1 1
4 2
4 3
4 5
2 4
3 4
7 4
8 4
9 4
7 5
8 5
9 5
7 6
8 6
9 6
10 10 3
5 5
4 4
6 6
5 3 6
0 2
1 2
2 2
3 2
4 2
4 0
'''