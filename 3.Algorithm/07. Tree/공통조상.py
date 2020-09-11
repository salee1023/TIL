def size(pp):
    global cnt
    if pp:
        cnt += 1
        size(tree[pp][0])
        size(tree[pp][1])

def find(n1, n2):
    n1_a, n2_a = [], []
    while tree[n1][2]:
        n1_a.append(tree[n1][2])
        n1 = tree[n1][2]
    while tree[n2][2]:
        n2_a.append(tree[n2][2])
        n2 = tree[n2][2]
    for i in range(len(n1_a)):
        if n2_a.count(n1_a[i]):
            return n1_a[i]
# ---------------------------------------------
T = int(input())
for tc in range(1, 1+T):
    V, E, n1, n2 = map(int, input().split())
    arr = list(map(int, input().split()))
    tree = [[0]*3 for _ in range(V+1)]
    cnt = 0
    for i in range(E):
        p, c = arr[i*2], arr[i*2+1]
        if tree[p][0]: tree[p][1] = c
        else: tree[p][0] = c
        tree[c][2] = p

    pp = find(n1, n2) # 공통 조상 찾기
    size(pp) # 공통 조상 subtree의 크기
    print(f'#{tc} {pp} {cnt}')

'''
1
13 12 8 13
1 2 1 3 2 4 3 5 3 6 4 7 7 12 5 9 5 8 6 10 6 11 11 13
'''