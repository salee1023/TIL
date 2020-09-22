T = int(input())
for tc in range(1, 1+T):
    N, M, K = map(int, input().split()) # NxM, K: 사각 테두리 한 변의 길이
    arr = [list(map(int, input().split())) for _ in range(N)]
    res = [] # 테두리의 합을 넣어줄 배열
    # 테두리의 시작점
    for i in range(N-K+1):
        for j in range(M-K+1):
            s = 0
            # 사각 테두리 한 변의 길이만큼 꽉 채운 정사각형 합 구하기
            for x1 in range(i, i+K):
                for y1 in range(j, j+K):
                    s += arr[x1][y1]
            # 사각 테두리를 제외한 안쪽 정사각형 부분 값 빼기
            for x2 in range(i+1, i+K-1):
                for y2 in range(j+1, j+K-1):
                    s -= arr[x2][y2]
            # 각 테두리의 값을 배열에 저장
            res.append(s)
    print(f'#{tc} {max(res)-min(res)}')

# Test Case
'''
3
3 3 3
1 2 3
4 5 6
7 8 9
4 4 3
2 3 4 3
5 6 7 8
9 7 9 7
1 2 4 5
6 5 4
11 75 97 9 36
14 33 72 12 57
44 77 38 98 67
38 30 69 16 48
45 29 35 64 56
23 75 48 87 45
'''