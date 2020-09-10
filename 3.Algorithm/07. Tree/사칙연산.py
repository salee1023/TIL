def cal(i):
    if tree[i][1] == 0: # 숫자
        return tree[i][0]
    else: # 연산자
        left, right = cal(tree[i][1]), cal(tree[i][2])
        if tree[i][0] == '+': return left + right
        elif tree[i][0] == '-': return left - right
        elif tree[i][0] == '*': return left * right
        else: return left / right
# ----------------------------------------
for tc in range(1, 11):
    N = int(input())
    tree = [[0]*3 for _ in range(N+1)]
    ans = 0
    for _ in range(N):
        arr = input().split()
        i = int(arr[0])
        if len(arr) > 3:
            tree[i][0], tree[i][1], tree[i][2] = arr[1], int(arr[2]), int(arr[3])
        else:
            tree[i][0] = int(arr[1])
    print(f'#{tc} {round(cal(1))}')
