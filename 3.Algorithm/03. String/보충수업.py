month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

T = int(input())
for tc in range(1,T+1):
    ymd = input()
    y = int(ymd[0:4])
    m = int(ymd[4:6])
    d = int(ymd[6:8])
    if 0 < m <= 12:
        if 0 < d <= month[m]:
            print('#%d %04d/%02d/%02d'%(tc, y, m, d))
    else:
        print(f'#{tc} -1')




