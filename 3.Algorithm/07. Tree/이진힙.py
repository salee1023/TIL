def make_h(N):
    global heap_c
    for n in range(1, N+1):
        heap[n] = arr[n-1]
        p = n // 2
        while p and heap[p] > heap[n]:
            heap[p], heap[n] = heap[n], heap[p]
            p //= 2
            n //= 2
# ---------------------------------------
T = int(input())
for tc in range(1, 1+T):
    N = int(input())
    arr = list(map(int, input().split()))
    heap = [0]*(N+1)
    res = 0
    make_h(N)
    p = N //2
    while p:
        res += heap[p]
        p //= 2
    print(f'#{tc} {res}')

'''
heapq 사용
import heapq
T = int(input())
for tc in range(1, 1+T):
    N = int(input())
    heap = []
    arr = list(map(int, input().split()))
    for i in range(len(arr)):
        heapq.heappush(heap, arr[i])
    heap = [0]+heap
    res = 0
    p = N // 2
    while p:
        res += heap[p]
        p //= 2
    print(f'#{tc} {res}')
'''
