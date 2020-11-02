def correct(i, n, mistake): # n진수 한자리씩 수정하는 함수
    temp = mistake[:]
    temp[i//n] = str(i % n)
    ans = ''.join(temp)
    return ans


def compare():
    for b in range(len(binary)*2):
        new_binary = correct(b, 2, binary)
        for t in range(len(ternary)*3):
            new_ternary = correct(t, 3, ternary)
            if int(new_binary, 2) == int(new_ternary, 3):
                print(f'#{tc} {int(new_binary, 2)}')
                return

#--------------------------------------------------
T = int(input())
for tc in range(1, 1+T):
    binary = list(input())
    ternary = list(input())
    compare()