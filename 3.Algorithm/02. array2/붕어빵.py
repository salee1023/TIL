def reservation(c_time, N, M, K):
    ans = 'Possible'
    for n in range(N):
        # 손님이 온 시간에 만들어져있는 붕어빵의 개수
        fish = c_time[n]//M*K-n
        if fish < 1:
            ans = 'Impossible'
            break
        else:
            continue
    return ans

T = int(input())
for tc in range(1,T+1):
    N, M, K = map(int, input().split())
    # 예약 손님 list
    c_time = sorted(list((map(int, input().split()))))
    print(f'#{tc} {reservation(c_time, N, M, K)}')
