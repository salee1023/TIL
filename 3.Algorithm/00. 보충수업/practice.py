arr = [1,2,3,4,5]
tmp = arr[0]
for n in range(4):
    arr[n] = arr[n+1]
arr[4] = tmp
print(arr)
