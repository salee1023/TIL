T = int(input())
for tc in range(1,1+T):
    N = int(input())
    farm = [input() for _ in range(N)]


    center = N//2
    count = 0
    for i in range(center+1):
        string = farm[i][center-i:center+i+1]
        for s in string:
            count += int(s)
    for i in range(center+1, N):
        string = farm[i][center-(N-1-i):center+(N-i)]
        for s in string:
            count += int(s)

    print(f'#{tc} {count}')

