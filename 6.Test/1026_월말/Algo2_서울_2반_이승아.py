def cases(N):
    # 돌을 밟으면 1, 안 밟으면 0
    # N개의 돌을 밟는 모든 경우의 수를 구한다.
    for i in range(1, 1 << N):
        ans = ''
        for j in range(N):
            if i & (1 << j):
                ans += '1'
            else:
                ans += '0'
        cases_1.append(ans)


def is_val(c):
    # 0이 연속해서 나오면 (2개의 돌을 건너뛰어야 하면) False
    for i in range(len(c)-1):
        if c[i] == '0' and c[i+1] == '0':
            return False
    # 모든 돌을 밟거나 1개의 돌을 건너뛰는거면 True
    else:
        return True

#----------------------------------------------
T = int(input())
for tc in range(1, 1+T):
    # N: 돌의 갯수, M: 돌을 밟는 횟수
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))

    # 징검다리를 건너는 모든 경우의 수를 구한다.
    cases_1 = []
    cases(N)

    # M번 돌을 밟는 경우의 수만 남긴다.
    cases_2 = []
    for c in cases_1:
        if c.count('1') == M:
            cases_2.append(c)

    # 돌을 연속으로 2번 밟는 경우의 수는 제거한다.
    cases_3 = []
    for c in cases_2:
        if is_val(c):
            cases_3.append(c)

    # 모든 조건을 만족하는 경우의 수 중에서 최대 점수를 구한다.
    max = 0
    for c in cases_3:
        ans = 0
        for i in range(len(c)):
            if c[i] == '1':
               ans += arr[i]
        if ans > max:
            max = ans
    print(f'#{tc} {max}')
