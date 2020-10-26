def find_code(N, M):
    for i in range(N):
        for j in range(M-1, -1, -1):
            if arr[i][j] == '1':
                return arr[i][j-55:j+1]


def solve_code(code):
    answer = ''
    for i in range(8):
        mini_code = code[i*7:i*7+7]
        mini_code_solve = ''
        cnt = 1
        for j in range(6):
            if mini_code[j] == mini_code[j+1]:
                cnt += 1
            else:
                mini_code_solve += str(cnt)
                cnt = 1
        else:
            mini_code_solve += str(cnt)
            for p in range(10):
                if password[p] == mini_code_solve:
                    answer += str(p)
    return answer


def verify(answer):
    ans = 0
    for i in range(7):
        if (i+1) % 2:
            ans += int(answer[i])*3
        else:
            ans += int(answer[i])
    ans += int(answer[7])
    if ans % 10:
        return 0
    else:
        ans = 0
        for i in range(8):
            ans += int(answer[i])
        return ans


#--------------------------------------------------------------------------------------------
password = ['3211', '2221', '2122', '1411', '1132', '1231', '1114', '1312', '1213', '3112']
T = int(input())
for tc in range(1, 1+T):
    N, M = map(int, input().split())
    arr = [input() for _ in range(N)]
    # 암호코드 추출하기
    code = find_code(N, M)
    # 암호 풀기
    answer = solve_code(code)
    # 암호 검증하기
    ans = verify(answer)
    print(f'#{tc} {ans}')