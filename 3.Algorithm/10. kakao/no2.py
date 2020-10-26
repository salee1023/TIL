'''
["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]
[2,3,4]
["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"]
[2,3,5]
["XYZ", "XWY", "WXA"]
[2,3,4]
'''

def solution(orders, course):
    answer = []
    for c in course:
        menu_dict = {}
        for order in orders:
            arr = []
            arr.extend(order)
            n = len(arr)
            # 부분집합 생성
            for i in range(1, 1 << n):
                temp = []
                for j in range(12):
                    if i & (1 << j):
                        temp.append(arr[j])
                if len(temp) == c:
                    temp.sort()
                    m = ''.join(temp)
                    if m in menu_dict.keys():
                        menu_dict[m] += 1
                    else:
                        menu_dict[m] = 1
        else:
            if len(menu_dict) > 0:
                val = max(menu_dict.values())
                if val >= 2:
                    for m in menu_dict.keys():
                        if menu_dict[m] == val:
                            answer.append(m)
    answer.sort()
    return answer

orders = ["XYZ", "XWY", "WXA"]
course = [2, 3, 4]
print(solution(orders, course))
