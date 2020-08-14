# 0721_homework

### 1. Mutable & Immutable

> 주어진 컨테이너들을 각각 변경 가능한 것과 변경 불가능한 것으로 분류하시오
> String, List, Tuple, Range, Set, Dictionary

- Mutable : List, Set, Dictionary
- Immutable : String, Tuple, Range



### 2. 홀수만 담기

> range와 slicing을 활용하여 1부터 50까지의 숫자 중, 홀수로만 이루어진 리스트를 만드시오

```python
odd_numbers = list(range(1,51,2))
print(odd_numbers)
```



### 3. Dictionary 만들기

> 반 학생들의 정보를 이용하여 key는 이름, value는 나이인 dictionary를 만드시오.

```python
class_info = {
    '강석민' : 28,
    '강채원' : 25,
    '구영지' : 27,
    '김대중' : 27,
    '김수연' : 26,
    '김수진' : 26,
    '이석원' : 28,
    '이승아' : 25
}
```



### 4. 반복문으로 네모 출력

> 두 개의 정수 n과 m이 주어졌을 때, 가로의 길이가 n, 세로의 길이가 m인 직사각형 형태의 별 (*)과 반복문을 이용해 출력하시오.

```python
n = 5 
m = 9

for i in range(9):
    for j in range(5):
        print('*', end ='')
    print() 
```



### 5.  조건 표현

> 주어진 코드의 조건문을 조건 표현식으로 바꾸어 작성하시오

```python
temp = 36.5
if temp >= 37.5:
    print('입실 불가')
else:
    print('입실 가능')
```

```python
print('입실 불가') if temp >= 37.5 else print('입실 가능') 
```





### 6. 평균 구하기

> 주어진 list에 담긴 숫자들의 평균값을 출력하시오.

```python
scores = [80, 89, 99, 83]
print(sum(scores)/len(scores))
```
