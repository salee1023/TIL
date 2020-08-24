ailen = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
T = int(input())
for t in range(1,T+1):
    tn, N = input().split()
    string = input()
    print(tn)
    for a in ailen:
        print(string.count(a)*(a+' '), end='')
