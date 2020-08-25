# 패턴이 문자열에 있는 지 판단(Brute Force)
def stringcmp(P,S):
    s = p = 0
    while s < len(S) and p <len(P):
        if P[p] != S[s]:
            s = s - p
            p = -1
        s += 1
        p += 1
    if p == len(P):
        return 1 # 검색 성공
    else:
        return 0 # 검색 실패

# -----------------------------
T = int(input())
for tc in range(1,1+T):
    pattern = input()
    string = input()
    print(f'#{tc} {stringcmp(pattern,string)}')