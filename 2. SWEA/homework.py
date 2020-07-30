case = int(input())

for i in range(1, case+1):
    repeatstr = input()
    newstrs = []
    checkpoint = []
    idx = 0
    newstrs.append(repeatstr[0])
    for letter in repeatstr[1:]:
        print(letter)
