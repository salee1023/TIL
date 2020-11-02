# List 1 (Problems)

#### 문제 01) 4828. [파이썬 S/W 문제해결 기본] 1일차 - min max

#### 풀이 01) 

✔ list 자료형에 익숙해지기위해, `min` , `max` 메소드를 사용하지 않았다.

✔ list 요소를 순차적으로 조회하면서,  최솟값과 최댓값을 찾는다.

```python
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    
    # list의 처음값을 기준으로 다른 요소들과 비교한다.
    min = max = arr[0]
    for num in arr:
        if num < min:
            min = num
        elif num > max:
            max = num
    print(f'#{tc} {max-min}')
```

---

#### 문제 02) 4831. [파이썬 S/W 문제해결 기본] 1일차 - 전기버스

#### 풀이 02) 

```python
T = int(input())
for tc in range(1, T+1):
    K, N, M = map(int, input().split())
    # 충전소
    charger = list(map(int, input().split()))

    last = 0
    cnt = 0
    while last+ K < N: # 종점에 도착하지 않았으면
        for i in range(K,0,-1): # 한번에 갈 수 있는 거리에 충전소가 있을 때
            if (last + i) in charger:
                cnt += 1
                last += i
                break
        else: # 한번에 갈 수 있는 거리에 충전소가 없을 때
            print(f'#{tc} 0')
            break
    else: # 종점 도착
        print(f'#{tc} {cnt}')
```



