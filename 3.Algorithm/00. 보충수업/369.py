T = int(input())
arr = ['3','6','9']
for i in range(1, 1+T):
    count = 0
    s = str(i)
    count = s.count('3') + s.count('6') + s.count('9')
    if count:
        print('-'*count, end=' ')
    else:
        print(i, end=' ')