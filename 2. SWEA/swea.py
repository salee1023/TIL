case = int(input())

for c in range(1, case+1):
    n , m = map(int, input().split())
    total = 0

    # 2차원 list 생성
    array1 = []
    for _ in range(n):
        array1.append(list(map(int, input().split())))

    for numbers in array1:
        if numbers.count(1) >= m:
            count = 0
            for i in range(n-m+1):
                if numbers[i:i+m].count(1) == m:
                        count += 1
            if count == 1:
                total += 1

    # 행열 바꾼 array2 생성 
    array2 = []
    for idx in range(n):
        array2.append([i[idx] for i in array1])

    for numbers in array2:
        if numbers.count(1) >= m:
            count = 0
            for i in range(n-m+1):
                if numbers[i:i+m].count(1) == m:
                        count += 1
            if count == 1:
                total += 1 
    
    print(f'#{c} {total}')