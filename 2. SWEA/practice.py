array1 = [
    [0,0,1,1,1],
    [1,1,1,1,0],
    [0,0,1,0,0],
    [0,1,1,1,1],
    [1,1,1,0,1]
    ]
total = 0
for numbers in array1:
        if numbers.count(1) >= 3:
            for i in range(5-3+1):
                if numbers[i:i+3].count(1) == 3:
                        print(numbers[i:i+3])
array2 = []
for idx in range(5):
    array2.append([i[idx] for i in array1])

#for numbers in array1:
   #     if numbers.count(1) == m:
    #        for i in range(n-m+1):
     #           if numbers[i:i+n].count(1) == m:
      #                  total += 1

          
