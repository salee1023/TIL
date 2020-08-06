def SelectionSort(a, N):
    for i in range(N-1):
        if i%2 == 0: #최대
            max = i
            for j in range(i+1, N):
                if a[max] < a[j]:
                    max = j
            a[i], a[max] = a[max], a[i]
        else:
            min = i
            for j in range(i+1, N):
                if a[min] > a[j]:
                    min = j
            a[i], a[min] = a[min], a[i]

    for n in range(10):
        print(f'{a[n]} ' ,end='')
    return 0

T = int(input())
for tc in range(1, 1+T):
    N = int(input())
    arr = list(map(int, input().split()))
    print(f'#{tc} ',end='')
    SelectionSort(arr,N)
    print()


