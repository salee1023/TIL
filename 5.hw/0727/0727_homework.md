# 0727_homework

### 1. 모음은 몇 개나 있을까?

> 문자열을 전달 받아 해당 문자열의 모음 갯수를 반환하는 count_vowels 함수를 작성하시오. 단 .count() 메서드를 활용하여 작성하시오.

```python
def count_vowels(words):
    # 모음 리스트 생성
    vowels = ['a', 'e', 'i', 'o', 'u']
    count = 0
    # words에 모음이 있는지 탐색
    for vowel in vowels:
        count += words.count(vowel)
    return print(count)

count_vowels('apple')
count_vowels('banana')    
```







### 2. 문자열 조작

> 다음 중, 문자열(string)을 조작하는 방법으로 옳지 않은 것을 고르시오.

(1) .find(x) 는 x의 첫번째 위치를 반환한다. 없으면 -1을 반환한다. (참)

(2) .split([chars]) 은 특정 문자를 지정하면 문자열을 특정 문자를 기준으로 나누어 list로 반환한다. 특정 문자를 지정하지 않으면 공백을 기준으로 나눈다. (참)

(3) .replace(old, new[,count])는 바꿀 대상 문자를 새로운 문자로 바꿔서 반환한다. (참)

(4) .strip([chars])은 특정 문자를 지정하면, 양쪽에서 해당 문자를 찾아 제거한다. 특정 문자를 지정하지 않으면 오류가 발생한다. (거짓) 오류안남. 





### 3. 정사각형만 만들기

> 각각 너비와 높이의 값으로 이루어진 2개의 list를 전달 받아, 각각의 값들을 조합하여 만들 수 있는 정사각형만의 넓이를 담은 list를 반환하는 only_square_area 함수를 작성하시오.

```python
def only_square_area(list1, list2):
    # 정사각형 넓이를 담을 list 선언
    square_area = []
    for i in list1:
        for j in list2:
            # 너비와 높이가 같을 때, 넓이 계산
            if i == j:
                square_area.append(i*j)
    return print(square_area)

only_square_area([32, 55, 63], [13, 32, 40, 55])
```







