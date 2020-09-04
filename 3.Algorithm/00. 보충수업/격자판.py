# 7자리 숫자 만들기
def make(i, j, length, numbers):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    if length == 7: # 7자리 완성
        if numbers not in check: # 이전에 만든 숫자와 같은지 비교
            check.append(numbers)
    else:
        for d in range(4):
            ni, nj = i + dx[d], j+dy[d]
            if 0 <= ni < 4 and 0 <= nj < 4:
                make(ni, nj, length+1, numbers+arr[ni][nj])

# ---------------------------------------------
T = int(input())
for tc in range(1,1+T):
    arr = [input().split() for _ in range(4)]
    check = []
    for i in range(4):
        for j in range(4):
            # 시작 지점 (좌표 i, j / 길이 1 / 처음 숫자 arr[i][j])
            starti, startj = i, j
            length = 1
            numbers = arr[i][j]
            make(i, j, length, numbers)
    print(f'#{tc} {len(check)}')