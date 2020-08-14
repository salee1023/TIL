# 0730_homework

### 1.  Circle  인스턴스 만들기

```python
class Circle:
    pi = 3.14
    x = 0
    y = 0
    r = 0

    def __init__(self, r, x, y):
        self.r = r
        self.x = x
        self.y = y
	
    # 넓이
    def area(self):
        return self.pi * self.r * self.r

    # 둘레
    def circumference(self):
        return 2 * self.pi * self.r
	
    # 좌표
    def center(self):
        return (self.x, self.y)


c1 = Circle(3, 2, 4)
print(c1.area())
print(c1.circumference())       
```

```
28.259999999999998
18.84
```







### 2. Dog와 Bird는 Animal이다

```python
class Animal:
    def __init__(self, name):
        self.name = name

    def walk(self):
        print(f'{self.name}! 걷는다!')

    def eat(self):
        print(f'{self.name}! 먹는다!')

class Dog(Animal):
    def __init__(self, name):
        self.name = name
	# method overriding
    def walk(self):
        print(f'{self.name}! 달린다!')    

    def bark(self):
        print(f'{self.name}! 짖는다!')

class Bird(Animal):
    def __init__(self, name):
        self.name = name
    
    def fly(self):
        print(f'{self.name}! 푸드덕!')


dog = Dog('멍멍이')
dog.walk()
dog.bark()

bird = Bird('구구')
bird.walk()
bird.eat()
bird.fly()
```

```
멍멍이! 달린다!
멍멍이! 짖는다!
구구! 걷는다!
구구! 먹는다!
구구! 푸드덕!
```



### 3. 오류의 종류

- `ZeroDivisionError` : '0'으로 숫자를 나눌 때 발생한다.

```python
print(5/0)
```

```
Traceback (most recent call last):
  File "homework4.py", line 1, in <module>
    print(5/0)
ZeroDivisionError: division by zero
```

- `NameError` : 변수가 정의되지 않았을 때 발생한다. 

```python
print(name)
```

```
Traceback (most recent call last):
  File "homework4.py", line 1, in <module>
    print(name)
NameError: name 'name' is not defined
```

- `TypeError` : 타입이 다른 변수끼리 연산하려 할 때 발생한다. (자동 형변환 제외)

```python
a = '123'
print(1+a)
```

```
Traceback (most recent call last):
  File "homework4.py", line 2, in <module>
    print(1+a)
TypeError: unsupported operand type(s) for +: 'int' and 'str'
```

- `IndexError` : 범위를 넘어가는 인덱스를 조회할 때 발생한다.

```python
a = [1,2,3,4,5]
print(a[5])
```

```
Traceback (most recent call last):
  File "homework4.py", line 2, in <module>
    print(a[5])
IndexError: list index out of range
```

- `KeyError` : 딕셔너리에 없는 key로 접근할 때 발생한다.

```python
a = {'1반':10, '2반':20}
print(a['3반'])
```

```
Traceback (most recent call last):
  File "homework4.py", line 2, in <module>
    print(a['3반'])
KeyError: '3반'
```

- `ModuleNotFoundError` : 모듈의 이름이 잘못되었을 때 발생한다.

```python
import randoms
a = random.choice([1,2,3,4,5])
print(a)
```

```
Traceback (most recent call last):
  File "homework4.py", line 1, in <module>
    import randoms
ModuleNotFoundError: No module named 'randoms'
```

- `ImportError` : 패키지는 찾았지만, 안에 import하려는 모듈이 없을 때 발생한다.

```python
# Animal.py
class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

# example.py
from Animal import Bird
```

```
Traceback (most recent call last):
  File "homework4.py", line 1, in <module>
    from Animal import Bird
ImportError: cannot import name 'Bird' from 'Animal'
```













