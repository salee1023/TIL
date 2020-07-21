# 0721_workshop

### 1. 간단한 N의 약수 (SWEA #1933)

```python
# 입력으로 1개의 정수 N이 주어진다. 정수 N의 약수를 오름차순으로 출력하는 프로그램을 작성하시오.
num = int(input())

for i in range(num):
    if num % (i+1) == 0:
        print((i+1), end =' ')
```



### 2. 중간값 찾기 (SWEA #2063 변형)

```python
# 집단의 수치를 크기 순으로 배열 했을 때 전체의 중앙에 위치하는 수치를 구하시오.
numbers = [
    85, 72, 38, 80, 69, 65, 68, 96, 22, 49, 67,
    51, 61, 63, 87, 66, 24, 80, 83, 71, 60, 64,
    52, 90, 60, 49, 31, 23, 99, 94, 11, 25, 24
]

new_numbers = sorted(numbers)
mid_idx = int(len(new_numbers)/2)

print(new_numbers[mid_idx])  
```



### 3. 계단 만들기

```python
# 자연수 number를 입력 받아, 높이가 number인 내려가는 계단을 출력하시오.
number = int(input())

for i in range(number):
    for j in range(number):
        if j <= i:
            print(j+1, end = ' ')          
    print('\n')   
```



### 4. 구구단을 외자, 구구단을 외자 2 X 1?!

```python
# 2단부터 9단까지 for문을 사용하여 구구단을 출력하시오.
for i in range(2,10):
    print(f'--------[{i}단]---------')
    for j in range(1,10):
        print(f'{i} X {j} = {i*j}')
```



