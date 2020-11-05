from collections import deque

for t in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    # M <= 1,000,000 이므로, 1,000,001 크기의 중간연산결과 list 생성
    visited = [0] * 1000001
    Q = deque()
    Q.append(N)
    while Q:
        n = Q.popleft()
        next_ns = [n+1, n-1, n*2, n-10]
        if n == M:
            break
        for next_n in next_ns:
            if 1 <= next_n <= 1000000 and visited[next_n] == 0:
                Q.append(next_n)
                visited[next_n] = visited[n] + 1
    print(f'#{t} {visited[M]}')