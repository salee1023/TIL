T = int(input())
for tc in range(1, 1+T):
    N, numbers = input().split()
    N = int(N)
    print(f'#{tc} ', end='')
    for n in range(N):
        t = format(int(numbers[n], 16), '03b')
        # if len(t) < 4:
        #     print('0'*(4-len(t)), end='')
        print(t, end='')
    print()


'''
3
4 47FE
5 79E12
8 41DA16CD
'''