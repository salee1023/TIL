def G(card, i, j):
    if i == j:  return i
    else:
        n1, n2 = G(card, i, (i+j)//2), G(card, (i+j)//2+1, j)
        a = card[n1-1]
        b = card[n2-1]
        if a > b:
            if a == 3 and b == 1:   return n2
            else:   return n1
        elif a < b:
            if a == 1 and b == 3:   return n1
            else:   return n2
        else:   return n1

T = int(input())
for tc in range(1,1+T):
    N = int(input())
    card = list(map(int,input().split()))
    print(f'#{tc} {G(card, 1, N)}')