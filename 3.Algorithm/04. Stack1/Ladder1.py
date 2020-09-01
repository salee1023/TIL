# finish에서 올라가서 start 확인하기
def ladder(f): # f : finish
    d = 99 # d : 깊이
    while d > 0: # 시작점으로 올라올 때 까지
        if f-1 >= 0 and G[d][f-1] == 1: # 왼쪽에 사다리가 있으면
            # 사다리가 끝날 때 까지 왼쪽으로 간다
            while f-1 >= 0 and G[d][f-1] == 1:
                f -= 1
        elif f+1 <= 99 and G[d][f+1] == 1: # 오른쪽에 사다리가 있으면
            # 사다리가 끝날 때 까지 오른쪽으로 간다
            while f+1 <= 99 and G[d][f+1] == 1:
                f += 1
        # 좌우에 사다리가 없으면 위로 올라간다
        d -= 1

    # d == 0 일 때, f가 start
    return f
# ----------------------------------------------------------------
for _ in range(1):
    T = int(input())
    G = [list(map(int, input().split())) for _ in range(100)]
    finish = G[99].index(2) # 도착 지점
    print(f'#{T} {ladder(finish)}')