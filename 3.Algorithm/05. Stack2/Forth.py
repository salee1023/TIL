def cal(arr):
    cal = ['+', '-', '*', '/']
    stack = []
    ans = 0
    for a in arr:
        if a =='.':
            if len(stack) > 1:
                return 'error'
        elif a in cal:  # 연산자이면
            if len(stack) < 2:
                return 'error'
            else:
                x = int(stack.pop())
                y = int(stack.pop())
                if a == '+':
                    ans = y + x
                    stack.append(ans)
                elif a == '-':
                    ans = y - x
                    stack.append(ans)
                elif a == '*':
                    ans = y * x
                    stack.append(ans)
                elif a == '/':
                    ans = y // x
                    stack.append(ans)
        else:  # 숫자이면
            stack.append(a)
    else:
        return ans

# ----------------------------------
T = int(input())
for tc in range(1,1+T):
    arr = list(input().split())
    print(f'#{tc} {cal(arr)}')
