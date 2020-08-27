def check(sentence):
    stack = []
    ans = 1
    for s in sentence:
        if s in '{(': stack.append(s)
        elif s == '}':
            if len(stack) == 0 or '{' != stack[-1]: # 스택이 비어있거나 맨 위 글자와 다를 때
                return 0
            else: stack.pop()    
        elif s == ')': 
            if len(stack) == 0 or '(' != stack[-1]:
                return 0
            else: stack.pop()
    
    if stack: return 0
    else: return ans

# ----------------------------
T = int(input())
for tc in range(1, 1+T):
    sentence = input()
    print(f'#{tc} {check(sentence)}')
            


