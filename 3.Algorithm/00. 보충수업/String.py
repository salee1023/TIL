def count(P, S):
    c = 0
    l = len(P)
    for i in range(len(S)):
        if S[i:i+l] == P:
            c += 1
    return c
# -----------------------------------------
for _ in range(10):
    tc = int(input())
    pattern = input()
    string = input()
    print(f'#{tc} {count(pattern, string)}')