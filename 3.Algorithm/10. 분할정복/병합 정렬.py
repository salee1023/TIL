def merge_sort(arr):
    global cnt
    # 분할
    if len(arr) == 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    # 병합
    merged = []
    l = r = 0
    while l < len(left) and r < len(right):
        if left[l] <= right[r]:
            merged.append(left[l])
            l += 1
        else:
            merged.append(right[r])
            r += 1
    # 오른쪽이 먼저 모두 복사되었을 때 (왼쪽 list가 남아있을 때)
    if left[l:]:
        cnt += 1
    merged.extend(left[l:])
    merged.extend(right[r:])
    return merged

# -------------------------------------------
T = int(input())
for tc in range(1, 1+T):
    N = int(input())
    arr = list(map(int, input().split()))
    cnt = 0
    merged = merge_sort(arr)
    print(f'#{tc} {merged[N//2]} {cnt}')