# 아래에서 위로 올라가기
def ladder(f): # f : finish좌표
    cnt = 0 # 이동 거리
    d = 99 # d : 깊이
    while d > 0: # 시작점으로 올라올 때 까지
        if f-1 >= 0 and G[d][f-1] == 1: # 왼쪽에 사다리가 있으면
            # 사다리가 끝날 때 까지 왼쪽으로 간다
            while f-1 >= 0 and G[d][f-1] == 1:
                f -= 1
                cnt += 1
        elif f+1 <= 99 and G[d][f+1] == 1: # 오른쪽에 사다리가 있으면
            # 사다리가 끝날 때 까지 오른쪽으로 간다
            while f+1 <= 99 and G[d][f+1] == 1:
                f += 1
                cnt += 1
        # 좌우에 사다리가 없으면 위로 올라간다
        d -= 1
        cnt += 1
    return f, cnt
# ----------------------------------------------------------------
for _ in range(10):
    T = int(input())
    G = [list(map(int, input().split())) for _ in range(100)]
    min = 10000
    ans = 0
    for i in range(100):
        if G[99][i] == 1: # 마지막지점
            f, cnt = ladder(i)
            if cnt < min:
                min = cnt
                ans = f
    print(f'#{T} {ans}')