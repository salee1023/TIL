'''
1단계 new_id의 모든 대문자를 대응되는 소문자로 치환합니다.
2단계 new_id에서 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.)를 제외한 모든 문자를 제거합니다.
3단계 new_id에서 마침표(.)가 2번 이상 연속된 부분을 하나의 마침표(.)로 치환합니다.
4단계 new_id에서 마침표(.)가 처음이나 끝에 위치한다면 제거합니다.
5단계 new_id가 빈 문자열이라면, new_id에 "a"를 대입합니다.
6단계 new_id의 길이가 16자 이상이면, new_id의 첫 15개의 문자를 제외한 나머지 문자들을 모두 제거합니다.
     만약 제거 후 마침표(.)가 new_id의 끝에 위치한다면 끝에 위치한 마침표(.) 문자를 제거합니다.
7단계 new_id의 길이가 2자 이하라면, new_id의 마지막 문자를 new_id의 길이가 3이 될 때까지 반복해서 끝에 붙입니다.
'''
'''
"...!@BaT#*..y.abcdefghijklm"
"z-+.^."
"=.="
"123_.def"
"abcdefghijklmn.p"
'''

def solution(new_id):
    answer = ''
    first, second, third, forth = '', '', '', ''
    # 1st step
    first = new_id.lower()
    # 2nd step
    for n in first:
        x = ord(n)
        if 45 <= x <= 46 or 48 <= x <= 57 or x == 95 or 97 <= x <= 122:
            second += n
    # 3rd step
    if len(second) <= 1:
        third = second
    else:
        for i in range(len(second)-1):
            if second[i] != '.':
                third += second[i]
            else:
                if second[i+1] != '.':
                    third += second[i]
        if second[-1] != '.':
            third += second[-1]
    # 4th step
    temp = []
    temp.extend(third)
    if len(temp) == 0:
        forth = ''.join(temp)
    else:
        if temp[0] == '.':
            temp.pop(0)
        elif temp[-1] == '.':
            temp.pop(-1)
        forth = ''.join(temp)
    # 5th step, 6th step
    if len(forth) == 0:
        forth += 'a'
    elif len(forth) >= 16:
        forth = forth[:15]
        if forth[-1] == '.':
            forth = forth[:14]
    # 7th step
    if len(forth) <= 2:
        while len(forth) != 3:
            forth += forth[-1]
    answer = forth
    return answer

a = ""
print(solution(a))