def delete(sentence):
    stack = []
    for s in sentence:
        if len(stack) ==0 or stack[-1] != s:
            stack.append(s)
        else:
            stack.pop()    
    return stack
# --------------------------
T = int(input())
for tc in range(1,1+T):
    sentence = input()
    ans = delete(sentence)
    print(f'#{tc} {len(ans)}')
