def g_col(matrix,index):
    x = []
    for m in matrix:
        x.append(m[index-1])
    return x

A = [
    [1,2,3],
    [4,5,6]
]
B = [
    [1,2],
    [3,4],
    [5,6]
]
re_A = [list(i) for i in zip(*A)]
print(re_A)
