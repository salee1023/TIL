def f(i, sum):
    global min
    if sum >= min: # 합이 최솟값을 넘어가면 끝낸다
        return
    if i == N:
        if B <= sum: # 부분집합의 합이 선반보다 높으면 min update
            min = sum
        return
    v[i] = 1 # i번째 점원이 포함될 경우
    f(i+1, sum+h[i])
    v[i] = 0 # i번째 점원이 포함하지 않을 경우
    f(i+1, sum)
# ---------------------------------------
T = int(input())
for tc in range(1, 1+T):
    N, B = map(int, input().split()) # N: 점원 수, B: 선반 높이
    h = list(map(int, input().split()))
    v = [0]*N
    min = 1000000000
    f(0, 0)
    print(f'#{tc} {min-B}')