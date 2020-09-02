def findcard(cards):
    cp = [] # 카드 정보 기록
    for i in range(len(cards)//3):
        card = cards[3*i: 3*i+3]
        if card in cp: # 겹치는 카드가 있을 때
            return 'ERROR'
        cp.append(card) # 기록
        if card[0] == 'S':
            SDHC[0] += 1
        elif card[0] == 'D':
            SDHC[1] += 1
        elif card[0] == 'H':
            SDHC[2] += 1
        elif card[0] == 'C':
            SDHC[3] += 1
    else:
        return '%d %d %d %d' % (13-SDHC[0], 13-SDHC[1], 13-SDHC[2], 13-SDHC[3])
# -----------------------------------------
T = int(input())
for tc in range(1,1+T):
    SDHC = [0]*4
    cards = input()
    print(f'#{tc} {findcard(cards)}')