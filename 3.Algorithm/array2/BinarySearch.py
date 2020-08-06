def binarySearch(P, key):
    start = 1
    end = P
    cnt = 0
    while start <= end:
        mid = (start+end)//2
        if mid == key:
            return cnt
        elif mid > key:
            end = mid
            cnt += 1
        else:
            start = mid
            cnt += 1

T = int(input())
for tc in range(1,1+T):
    P, A, B = map(int, input().split())
    cntA = binarySearch(P,A)
    cntB = binarySearch(P,B)
    print(f'#{tc} ', end ='')
    if cntA > cntB:
        print('B')
    elif cntA < cntB:
        print('A')
    else:
        print('0')