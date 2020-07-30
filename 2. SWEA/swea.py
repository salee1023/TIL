case = int(input())

for c in range(1, case+1):
    # nxn 정사각형, m = 글자 수
    n , m = map(int, input().split())
    array1 = []
    array2 = []

    # 2차원 list 생성
    for t in range(n):
        array1.append(list(map(int, input().split())))
    # 행열 바꾼 array2 생성
    
    for idx in range(n):
        array2.append([i[idx] for i in array1])

    # array1, array2에 1이 연속 3번 나오면 result + 1
    count = 0
    for i in range(n):
        if (array1[i].count(1) == 3)  or (array2[i].count(1) == 3):
            count += 1  
        # 결과 출력
    print(f'#{t} {count}')