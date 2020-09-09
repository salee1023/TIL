def f(n): # n번 노드 방문, 방문 후 유효한 노드인지 검사
   if tree[n][0]: # 유효한 노드면
        f(tree[n][1]) # 왼쪽 자식으로 이동
        print(tree[n][0], end='') # n번 노드에서 할일 (왼쪽자식에서 리턴 후, 중위순회 in-order)
        f(tree[n][2]) # 오른쪽 자식으로 이동
# -------------------------------------
for tc in range(1, 11):
    N = int(input())
    tree = [[0]*3 for _ in range(N+1)]
    for i in range(1, N+1):
        data = input().split()
        tree[int(data[0])][0] = data[1]
        if len(data) > 2:
            tree[int(data[0])][1] = int(data[2])
            if len(data) > 3:
                tree[int(data[0])][2] = int(data[3])
    print(f'#{tc} ', end='')
    f(1)
    print()