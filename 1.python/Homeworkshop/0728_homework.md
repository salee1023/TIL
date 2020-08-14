# 0728_homework

### 1. Built-in 함수와 메서드

> sorted()와 . sort()의 차이점을 코드의 실행 결과를 활용하여 설명하시오.

`sorted()` 는 새로운 정렬된 리스트를 만든다.

`.sort()`  는 제자리에서 기존리스트를 정렬하고, `None`를 리턴한다.

```python
# 1. sorted()
numbers = [1, 3, 2, 5, 6, 7]
print(numbers, sorted(numbers))
print(type(sorted(numbers)))

# 2. .sort()
numbers2 = [3, 2, 6, 8, 10, 1, 2]
print(numbers2 , numbers2.sort())
print(type(numbers2.sort()))
```

```python
# 새롭게 정렬된 리스트가 생성되었다.
[1, 3, 2, 5, 6, 7] [1, 2, 3, 5, 6, 7]
<class 'list'>
# 기존 리스트가 정렬되고, None을 반환한다.
[1, 2, 2, 3, 6, 8, 10] None
<class 'NoneType'>
```



 

### 2. .extend()와 .append()

> .extend()와 .append()의 차이점을 코드의 실행 결과를 활용하여 설명하시오.

`.append()`  는 리스트에 값을 추가한다.

`.extend()` 는 순회가능(iterable)한 자료를 (`list` , `range`, `tuple`, `string`) 추가한다. 

```python
my_list = ['사과', '포도', '귤', '바나나', '망고']
my_list.append('복숭아')
print(my_list)

my_list2 = ['사과', '포도', '귤', '바나나', '망고'] 
my_list2.extend('복숭아')
print(my_list2)
```

```python
# .append()는 값을 추가한다
['사과', '포도', '귤', '바나나', '망고', '복숭아']
# .extend()는 '복숭아'를 iterable한 자료로 판단해, 각 글자를 값으로 추가한다.
['사과', '포도', '귤', '바나나', '망고', '복', '숭', '아']
```





### 3. 복사가 잘 된 건가?

> 아래의 코드를 실행하였을 때, 변수  a와 b에 담긴 list의 요소가 같은지 혹은 다른지 여부를 판단하고 그 이유를 작성하시오. 

```python
a = [1,2,3,4,5]
b = a

a[2] = 5

print(a)
print(b)
```

```python
[1, 2, 5, 4, 5]
[1, 2, 5, 4, 5]
```

a 와 b는 같은 id를 공유하기때문에 두 list의 요소는 같다.





