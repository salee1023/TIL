# 강의 보고 다시 쓰기
N = 10
A = [0 for _ in range(N)]
arr = [1,2,3,4,5,6,7,8,9,10]

def printSet(n, sum):
    global count
    if sum == 10:
        for i in range(n):
            if A[i] == 1:
                print("%d" % arr[i], end='')
        print()

def powerset(n,k,cursum):
    global total
    if cursum > 10: return
    total += 1
    if n == k:
        printSet(n,cursum)
    else:
        A[k] = 1
        powerset(n, k+1, cursum+arr[k])
        A[k] = 0
        powerset(n, k+1, cursum)

# -----------------------------------
powerset(N, 0, 0)
print("호출회수 : { }".format(total))