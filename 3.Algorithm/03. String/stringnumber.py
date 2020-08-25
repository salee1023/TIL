T = int(input())
for tc in range(1, 1+T):
    pattern = input()
    string = input()
    max_c = 0
    # pattern의 각 글자가 string에 몇 번 나오는 지 확인
    for p in pattern:
        c = 0
        for s in string:
            if s == p:
                c += 1
        if max_c <c:
            max_c = c
    print(f'#{tc} {max_c}')