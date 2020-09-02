def cal(S):
    stack = []
    res = 0
    for s in S:
        if s == '+':
            a, b = int(stack.pop()), int(stack.pop())
            stack.append(a+b)
        elif s == '*':
            a, b = int(stack.pop()), int(stack.pop())
            stack.append(a * b)
        else:
            stack.append(s)
    return stack.pop()

def transform(S):
    stack = [] # 연산자
    result = []
    for s in S:
        if s == '(':
            stack.append(s)
        elif s == '+':
            while stack[-1] == '*': # 우선 순위가 더 높은 '*'가 있으면
                result.append(stack.pop())
            stack.append(s)
        elif s == '*':
            stack.append(s)
        elif s == ')': # 여는 괄호를 만날 때 까지 모두 pop
            while stack[-1] != '(':
                result.append(stack.pop())
            stack.pop() # 남아있는 '(' 버리기
        else: # 숫자
            result.append(s)
    while stack: # stack에 남아있는 연산자 pop
        result.append(stack.pop())
    return result
# --------------------------------------------------------
for tc in range(1, 11):
    N = int(input())
    statement = input()
    new = transform(statement)
    print(f'#{tc} {cal(new)}')
