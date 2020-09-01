T = int(input())
for tc in range(1,1+T):
    N = int(input())
    arr = [[0]*10 for _ in range(10)]
    # 박스 색칠
    for n in range(N):
        r1, c1, r2, c2, c = map(int, input().split())
        for i in range(r1, r2+1):
            for j in range(c1, c2+1):
                if c == 1: # 빨강
                    arr[i][j] += 1
                else:
                    arr[i][j] += 2
    # 보라색 찾기
    count = 0
    for b in range(10):
        for b2 in range(10):
            if arr[b][b2] >= 3:
                count += 1
    print(f'#{tc} {count}')