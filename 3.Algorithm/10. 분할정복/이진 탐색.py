def b_search(num):
    global cnt
    start = ''
    l, r = 0, N-1
    while l <= r:
        mid = (l+r) // 2
        if arr[mid] == num:
            cnt += 1
            return
        elif arr[mid] < num: # 오른쪽
            now = 'r'
            l = mid + 1
        else: # 왼쪽
            now = 'l'
            r = mid - 1
        if start == now:
            return
        start = now
    return

# --------------------------------------------
T = int(input())
for tc in range(1, 1+T):
    N, M = map(int, input().split())
    arr = sorted(list(map(int, input().split())))
    find = list(map(int, input().split()))
    cnt = 0
    for num in find:
        b_search(num)
    print(f'#{tc} {cnt}')