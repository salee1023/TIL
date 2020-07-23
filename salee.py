case = int(input())
for i in range(1, case + 1):
    sum_data = 0
    for data in map(int, input().split()):
        if data % 2:
            sum_data += data
 
    print(f'#{i} {sum_data}')