T = int(input())
for tc in range(1,1+T):
    N, M, K, H = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    cnt = 0
    for i in range(N-2):
        for j in range(M-2):
            # 착륙장소
            spaceship = arr[i+1][j+1]
            n_arr = []
            for x in range(i, i+3):
                for y in range(j, j+3):
                    n_arr.append(arr[x][y])
            n_arr.remove(spaceship)
            # 착륙조건 확인
            m = max(n_arr)
            n = min(n_arr)
            if (m - n) <= K:
                if spaceship >= n and (spaceship - n) <= H:
                    cnt += 1

    print(f'#{tc} {cnt}')