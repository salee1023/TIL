'''
["java backend junior pizza 150",
"python frontend senior chicken 210",
"python frontend senior chicken 150",
"cpp backend senior pizza 260",
"java backend junior chicken 80",
"python backend senior chicken 50"]

["java and backend and junior and pizza 100",
"python and frontend and senior and chicken 200",
"cpp and - and senior and pizza 250",
"- and backend and senior and - 150",
"- and - and - and chicken 100",
"- and - and - and - 150"]
'''

def solution(info, query):
    answer = []
    l = len(info)
    table = [[0]*5 for _ in range(l+1)]
    # make table
    for i in range(len(info)):
        data = info[i].split()
        for j in range(4):
            table[i+1][j] = data[j]
        table[i+1][4] = int(data[4])
    # query 처리
    q = []
    for i in range(len(query)):
        condition = query[i].split()
        check = [i for i in range(1, l+1)]
        visit = [0] * (1+l)
        idx = 0
        for c in range(len(condition)-1):
            if condition[c] != 'and':
                q.append(condition[c])
            else:
                while q:
                    a = q.pop(0)
                    if a == '-':
                        for x in check:
                            visit[x] += 1
                    else:
                        for x in check:
                            if table[x][idx] == a:
                                visit[x] += 1
                else:
                    idx += 1
                    for x in range(1, 1+l):
                        if x in check and visit[x] != idx:
                            check.remove(x)

        else: # 소울푸드 check
            while q:
                a = q.pop(0)
                if a == '-':
                    for x in check:
                        visit[x] += 1
                else:
                    for x in check:
                        if table[x][3] == a:
                            visit[x] += 1
            else:
                for x in range(1, 1+l):
                    if x in check and visit[x] != 4:
                        check.remove(x)
        # 점수 check
        score = int(condition[-1])
        for x in check:
            if table[x][4] >= score:
                visit[x] += 1
        else:
            for x in range(1, 1+l):
                if x in check and visit[x] != 5:
                    check.remove(x)
        # 합격자 count
        answer.append(len(check))
    return answer