# 1.Python 기초

### 1-1.개요

- 버전 : Python 3.7
- 참고 : [Python 공식 Tutorial](https://docs.python.org/ko/3/)



### 1-2.기초 문법(Syntax)

##### 주석(Comment)

> 주석은 주로 함수나 클래스를 설명하기 위해 활용된다.

- 한 줄 주석은 `#` 으로 표현한다.

```python
# 이건 주석!
```

- 여러 줄의 주석은 `#` 을 줄마다 사용하거나,  `"""`, `'''` (multiline String)으로 표현한다. 

```python
'''
이건
여러줄에 걸쳐 쓸 수 있는
주석!!
'''
```



##### 코드 라인

- '1줄에 1문장'이 원칙
- 문장은 파이썬이 실행할 수 있는 최소한의 단위
- 보통 파이썬에서는 `;` 를 사용하지는 않지만, 한 줄로 표기할 때 예외적으로 사용

```python
# print문을 한 줄로 이어서 썼을 때, 오류 발생
print('hello') print('world') 
```

```python
File "<ipython-input-4-71f683e5cf02>", line 1
    print('hello')print('world')
                      ^
SyntaxError: invalid syntax
```

```python
# ;로 오류 해결
print('hello'); print('world')
```

```
hello
world
```



# 2. 변수 (Variable)

### 2-1. 변수

##### 할당 연산자 (Assignment Operator) : `=`

- 변수는 `=` 을 통해 할당(assignment) 된다.
- `type()` : 데이터 타입 확인
- `id()` : 메모리 주소 확인 

```python
# 변수에 값을 할당
a = 'salee'
type(a)
id(a)
```

```
str
140413408045016
```

- 같은 값과 다른값을 동시에 할당 할 수 있다. 

```python
# 같은 값을 동시에 할당
x = y = 'salee'
print(x)
print(y)

#다른 값을 동시에 할당
a,b = 7, 20
print(a)
print(b)
```

```
salee
salee
7
20
```



##### 식별자(Identifiers)



### 2-2. 데이터 타입 (Data Type)

##### 숫자 (Number)



##### 문자 (String)



##### 참/거짓 (Boolean)

