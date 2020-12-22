def solution(s):
    check = len(s) // 2
    p, y = 0, 0
    for i in range(len(s)):
        if p > check or y > check:
            return False
        if s[i] in ['p', 'P']:
            p += 1
        if s[i] in ['y', 'Y']:
            y += 1
    if p == y:
        return True
    else:
        return False

print(solution('pPoooyY'))