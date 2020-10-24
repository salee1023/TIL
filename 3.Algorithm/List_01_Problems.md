# List 1 (Problems)



#### 문제 01) [4828. [파이썬 S/W 문제해결 기본] 1일차 - min max](https://swexpertacademy.com/main/learn/course/lectureProblemViewer.do)

#### 풀이 01) 

```python
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    min = max = arr[0]
    for num in arr:
        if num < min:
            min = num
        elif num > max:
            max = num
    print(f'#{tc} {max-min}')
```

