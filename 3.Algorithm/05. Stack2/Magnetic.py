'''
7
1 0 2 0 1 0 1
0 2 0 0 0 0 0
0 0 1 0 0 1 0
0 0 0 0 1 2 2
0 0 0 0 0 1 0
0 0 2 1 0 2 1
0 0 1 2 2 0 2
'''
for tc in range(1,11):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    table = [list(arr[i][j] for i in range(N)) for j in range(N)]
    cnt = 0
    for t in table:
        for i in range(N):
            if t[i] == 1: # 빨간색
                move_i = i
                while move_i < N:
                    if t[move_i] == 2: # 다른 색의 자성체와 만나면 교착 cnt +1
                        cnt += 1
                        break
                    t[move_i] = 0 # 확인한 빨간색 자성체는 없애준다
                    move_i += 1
    print(f'#{tc} {cnt}')