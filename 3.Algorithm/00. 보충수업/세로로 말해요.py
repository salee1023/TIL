def read(arr, max):
    for i in range(max):
        for j in range(5):
            if len(arr[j]) <= i:
                continue
            else:
                print(f'{arr[j][i]}', end='')
# -------------------------------------
T = int(input())
for tc in range(1, 1+T):
    arr = [input() for _ in range(5)]
    max = 0
    for i in arr: # 최대 문자열의 길이
        if max < len(i):
            max = len(i)
    print(f'#{tc} ', end='')
    read(arr, max)
    print()

'''
2
ABCDE
abcde
01234
FGHIJ
fghij
AABCDD
afzz
09121
a8EWg6
P5h3kx
'''