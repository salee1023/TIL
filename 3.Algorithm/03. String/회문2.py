def is_pal(matrix,N,M):
    # 행
    for i in range(N):
        for j in range(N-M+1):
            string = matrix[i][j:j+M]
            if string == string[::-1]:
                return string
    # 열
    for i in range(N):
        for j in range(N-M+1):
            c_string = ''
            for m in range(M):
                c_string += matrix[j+m][i]
            if c_string == c_string[::-1]:
                return c_string
# ---------------------------------------------
T = int(input())
for tc in range(1, 1 + T):
    N, M = map(int, input().split())
    matrix = [input() for _ in range(N)]
    print(f'#{tc} {is_pal(matrix,N,M)}')