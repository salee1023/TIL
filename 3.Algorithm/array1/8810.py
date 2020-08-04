T = int(input())
for tc in range(1,1+T):
    N = int(input())
    sp = list(map(int, input().split()))

    # 줄기생성
    roots = []
    idx = 0
    for i in range(0,N-1):
        if sp[i] < sp[i+1]:
            continue
        else:
            if len(sp[idx:i+1]) > 1:
                roots.append(sp[idx:i+1])
            idx = i+1
    if len(sp[idx:N]) > 1:
        roots.append(sp[idx:N])

    #연산
    max_l = 0
    count = 0
    for r in roots:
        if len(r) > max_l:
            max_l = len(r)
            count = sum(r)
        elif len(r) == max_l:
                if sum(r) > count:
                    count = sum(r)

    print(f'#{tc} {len(roots)} {count}')