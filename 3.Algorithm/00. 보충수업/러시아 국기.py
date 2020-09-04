def count(w, b):
    global my_min
    c = 0
    for x in range(0, w+1): # white coloring
        for j in range(M):
            if flag[x][j] != 'W' and c < my_min:
                c += 1
    for y in range(w+1, b+1): # blue coloring
        for j in range(M):
            if flag[y][j] != 'B' and c < my_min:
                c += 1
    for z in range(b+1,N): # red coloring
        for j in range(M):
            if flag[z][j] != 'R' and c < my_min:
                c += 1
    my_min = c


def color(flag):
    for w in range(N-2): # 하얀색
        for b in range(w+1, N-1): # 파란색
            count(w, b)

# -------------------------------------
T = int(input())
for tc in range(1, 1+T):
    N, M = map(int, input().split())
    flag = [input() for _ in range(N)]
    my_min = N * M
    color(flag)
    print(f'#{tc} {my_min}')