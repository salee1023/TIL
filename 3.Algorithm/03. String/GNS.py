ailen = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
T = int(input())
for _ in range(T):
    test, s_num = input().split()
    num = int(s_num)
    arr = list(input().split())

    # 외계 숫자가 나온 수를 count배열에 넣는다.
    count = [arr.count(ailen[i]) for i in range(10)]

    # # count 배열에 저장된 수 만큼 ailen 숫자 출력한다.
    print(f'{test} ', end='')
    for i in range(10):
        print(count[i]*(ailen[i]+' '), end='')

# 다른 풀이
'''
ailen = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
T = int(input())
for t in range(1,T+1):
    tn, N = input().split()
    string = input()
    print(tn)
    for a in ailen:
        print(string.count(a)*(a+' '), end='')
'''