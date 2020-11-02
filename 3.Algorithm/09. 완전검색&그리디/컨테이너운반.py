T = int(input())
for tc in range(1, 1+T):
    N, M = map(int, input().split())
    weight = list(map(int, input().split()))
    volume = list(map(int, input().split()))
    weight.sort(reverse=True)
    volume.sort(reverse=True)
    w = v = res = 0
    while w < N and v < M:
        if volume[v] >= weight[w]:
            res += weight[w]
            v += 1
            w += 1
        else:
            w += 1
    print(f'#{tc} {res}')