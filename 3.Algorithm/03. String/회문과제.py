# 최대 회문 길이 확인하기
def pal(matrix):
    for l in range(100,1,-1): # 회문 길이
        for i in range(100):
            for j in range(100 - l + 1):
                s = matrix[i][j:j+l]
                if s == s[::-1]:
                    return l
# ---------------------------------------------
for _ in range(10):
    n = int(input())
    matrix = [input() for _ in range(100)]
    r_matrix = [[matrix[i][j] for i in range(100)] for j in range(100)] #전치행렬
    r = pal(matrix)
    c = pal(r_matrix)
    print(f'#{n} {max(r,c)}')