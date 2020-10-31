def exchange(x):
    global my_max
    new_num = int(''.join(number))
    # x만큼 바꾼 숫자가 memo에 있으면 return
    if new_num in memo[x]:
        return
    # memo에 없으면 memo[x]에 기록
    memo[x].append(new_num)
    # 주어진 횟수(cnt)만큼 숫자 자리 바꾸기
    if x == cnt:
        if new_num > my_max:
            my_max = new_num
        return
    else:
        for i in range(len(number)-1):
            for j in range(i+1, len(number)):
                number[i], number[j] = number[j], number[i]
                exchange(x+1)
                number[i], number[j] = number[j], number[i]

#-------------------------------------------
T = int(input())
for tc in range(1, 1+T):
    number, cnt = input().split()
    number = list(number)
    cnt = int(cnt)
    # 주어진 횟수 만큼 자리를 바꾼 숫자 기록
    memo = [[] for _ in range(cnt+1)]
    # 최대값
    my_max = 0
    exchange(0)
    print(f'#{tc} {my_max}')