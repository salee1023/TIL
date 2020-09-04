# Queue
T = int(input())
for tc in range(1,1+T):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    for _ in range(M):
        arr.append(arr.pop(0))
    print(f'#{tc} {arr[0]}')