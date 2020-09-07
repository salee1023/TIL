def change(idx,val):
    for j in range(idx, len(bit)):
        new[j] = val

def count(bit):
    c = 0
    for i in range(len(bit)):
        if new[i] != bit[i]:
            change(i, bit[i])
            c += 1
    return c
# ----------------------------
T = int(input())
for tc in range(1, 1+T):
    bit = input()
    new = ['0']*len(bit)
    print(f'#{tc} {count(bit)}')
