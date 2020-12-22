def solution(dartResult):
    BONUS = ['S', 'D', 'T']
    OPTIONS = ['*', '#']
    score = [0]*4
    s, b, o = 1, 1, 1
    for i in range(len(dartResult)):
        if dartResult[i] in BONUS:
            score[b] **= (BONUS.index(dartResult[i])+1)
            b += 1
        elif dartResult[i] in OPTIONS:
            index = s-1
            if dartResult[i] == '*':
                score[index] *= 2
                score[index-1] *= 2
            else:
                score[index] *= -1
        else:
            if dartResult[i-1] == '1':
                score[s-1] = 10
            else:
                score[s] = int(dartResult[i])
                s += 1
    answer = sum(score[1:])
    return answer

print(solution('10S#10S*10S'))