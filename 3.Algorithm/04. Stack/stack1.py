# C style
def push(item):
    global top
    if top > 100 -1:
        return
    else:
        top += 1
        stack[top] = item


def pop(): # isEmpty
    global top
    if top == -1:
        print("Stack is Empty!!")
        return
    else:
        result = stack[top]
        top -= 1
        return result
# ----------------------------
stack = [0]*100 # 고정
top = -1

push(1)
push(2)
push(3)

print(pop())
print(pop())
print(pop())