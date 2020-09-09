T = int(input())
for tc in range(1,1+T):
    x = int(input())
    money = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    print(f'#{tc}')
    for m in range(8):
        print(x // money[m], end=' ')
        x = x - (money[m]*(x//money[m]))
    print()