# 비율이 겹치는게 없음
ratio = {
    '211': '0',
    '221': '1',
    '122': '2',
    '411': '3',
    '132': '4',
    '231': '5',
    '114': '6',
    '312': '7',
    '213': '8',
    '112': '9'
}


def divide(c, b, a):
    minV = min(c, b, a)
    c = c // minV
    b = b // minV
    a = a // minV
    return str(c) + str(b) + str(a)


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [input() for _ in range(N)]
    test_list = [''] * N
    # 읽어서 2진수로
    for i in range(N):
        for j in range(M):
            test_list[i] += code[arr[i][j]]
    results = []
    visit = []
    ans = 0
    for y in range(N):

        a, b, c = 0, 0, 0
        # 바뀐 2진수 1, 0, 1 숫자 카운트 // 뒤 1 부터 카운트 0 될때 까지
        for x in range(M * 4 - 1, -1, -1):
            if b == 0 and c == 0 and test_list[y][x] == '1':
                a += 1
            elif a > 0 and c == 0 and test_list[y][x] == '0':
                b += 1
            elif a > 0 and b > 0 and test_list[y][x] == '1':
                c += 1
            # 어떤 비율이 있고, 다 세고 나면, 0이 오면?
            if a > 0 and b > 0 and c > 0 and test_list[y][x] == '0':
                # 거꾸로 -> 순서 제대로
                # 비율 제작
                temp = divide(c, b, a)
                # 비율 맞는 수 삽입
                results.append(ratio[temp])
                a = b = c = 0
            # 암호 찾은 경우에
            if len(results) == 8:
                # 순서 제대로
                results = results[::-1]
                # validation 한지 확인
                val = 3 * (int(results[0]) + int(results[2]) + int(results[4]) + int(results[6])) + \
                      (int(results[1]) + int(results[3]) + int(results[5]) + int(results[7]))
                # 처음 본 가능한 값이면 출력
                if (val % 10) == 0 and results not in visit:
                    # 반복하면서 출력할 값 계산
                    for s in range(len(results)):
                        ans += int(results[s])
                else:
                    # 한줄에 여러개 가능, 성공해도 비짓 넣고 반복 시작
                    # 아니면 visit에 기록
                    visit.append(results)
                    # 다시 반복 시작
                    results = []
                visit.append(results)
                results = []
    print("#{} {}".format(tc, ans))