# 1차원 배열 선택정렬
a = [7,4,2,3]
N = len(a)

for i in range(N-1):
    m = i
    for j in range(i+1,N):
         if a[m] > a[j]:
             m = j
    a[i], a[m] = a[m], a[i]
print(a)

# 2차원 배열 선택정렬
b = [[1,4],[2,1],[1,2]]
M = len(b)

# 행 순서
for i in range(M-1):
    m = i
    for j in range(i+1,M):
         if b[m][0] > b[j][0]:
             m = j
    b[i], b[m] = b[m], b[i]

# 넓이 먼저
for i in range(M-1):
    m = i
    for j in range(i+1,M):
         if b[m][0]*b[m][1] > b[j][0]*b[j][1]:
             m = j
    b[i], b[m] = b[m], b[i]

print(b)