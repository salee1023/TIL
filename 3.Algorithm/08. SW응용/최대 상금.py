def find_idx(tmp):
    for j in range(len(n) - 1, -1, -1):
        if tmp == number[j]:
            return j

#-------------------------------------------
T = int(input())
for tc in range(1, 1+T):
    n, c = input().split()
    number = []
    c = int(c)
    for i in range(len(n)):
        number.append(int(n[i]))

    i = 0
    while c and i < len(n)-1:
        tmp = max(number[i+1:])
        tmp_i = find_idx(tmp)
        if number[i] <= tmp:
            number[i], number[tmp_i] = number[tmp_i], number[i]
            c -= 1
        # elif number[i] >= tmp:
        #     c -= 1
        i += 1
    if c % 2:
        number[-1], number[-2] = number[-2], number[-1]

    print(f'#{tc} ', end='')
    for x in number:
        print(x, end='')
    print()


