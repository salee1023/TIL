def p(depth, n, res):

    if depth == n:
        new_op = ''.join(operator)
        if new_op in memo:
            return
        memo.add(new_op)
        if res in ans:
            return
        ans.append(res)
        return
    else:
        for i in range(depth, n):
            operator[i], operator[depth] = operator[depth], operator[i]
            # 자리 정해지면 숫자 계산
            if operator[depth] == '1':
                p(depth + 1, n, res + num[depth + 1])
            elif operator[depth] == '2':
                p(depth + 1, n, res - num[depth + 1])
            elif operator[depth] == '3':
                p(depth + 1, n, res * num[depth + 1])
            else:
                p(depth + 1, n, int(res / num[depth + 1]))
            operator[i], operator[depth] = operator[depth], operator[i]


# --------------------------------------------
T = int(input())
for tc in range(1, 1+T):
    N = int(input())
    cal = list(map(int, input().split()))
    num = list(map(int, input().split()))
    operator = []
    ans = []
    # 주어진 횟수 만큼 자리를 바꾼 숫자 기록
    memo = set()

    # 연산자 현황 파악하기
    for c in range(4):
        for _ in range(cal[c]):
            operator.append(str(c+1))

    # 연산자 순서 경우의 수 구하기 (순열)
    p(0, len(operator), num[0])
    print(f'#{tc} {max(ans)-min(ans)}')