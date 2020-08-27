def check(arr):
    for i in range(len(arr)):
        if arr[i] == '(':
            stack.append(arr[i])
        elif arr[i] == ')':
            if len(stack) == 0:
                return False
            else:
                stack.pop()
    if stack: return False
    else: return True
# ---------------------------------
stack = []
arr = "()()((())))"
print(check(arr))

