T = int(input())
for tc in range(1,1+T):
    N,M = map(int, input().split())
    carrots = list(map(int, input().split()))

    distance = 0
    box = M
    cp = 0
    while cp < N:
        if box <= carrots[cp]:
            carrots[cp] -= box
            distance += (cp+1)*2
            box = M
        else: # 당근의 개수가 더 적을 때
            box -= carrots[cp]
            carrots[cp] = 0
            cp += 1
    distance += N*2
    print(f'#{tc} {distance}')
