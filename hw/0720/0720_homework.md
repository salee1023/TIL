# 0720_homework

### 1. Python 예약어

```python
import keyword
print(keyword.kwlist)
```

```python
['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 
'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
```



### 2. 실수 비교

```python
import math

num1 = 0.1 *3
num2 = 0.3

math.isclose(num1, num2)
```



### 3. 이스케이프 시퀀스

- 줄 바꿈 : `\n`
- 탭 : `\t`
- 백슬래시 : `\\`



### 4. String Interpolation

```python
name = '철수'
print(f'안녕, {name}야')
```



### 5.  형 변환

```python
int('3.5')

---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
<ipython-input-21-6a27da1b269d> in <module>()
----> 1 int('3.5')

ValueError: invalid literal for int() with base 10: '3.5'
```

`String` 에서 ` integer`로 변환하려면 정수 형식에 맞아야 한다. 



### 6. 네모 출력

```python
n = 5
m = 9

print(('*'* n +'\n')*m)
```



### 7. 이스케이프 시퀀스 응용

```python
print('\"파일은 c:\\Windows\\Users\\내문서\\Python에 저장이 되었습니다.\" 나는 생각했다. \'cd를 써서 git bash로 들어가 봐야지.\'')
```



### 8. 근의 공식

```python
a = int(input('이차항의 계수:'))
b = int(input('일차항의 계수:'))
c = int(input('상수항:'))

d = (b ** 2) - (4*a*c)

if d > 0:
  answer1 = ((-b) + (d**0.5)) / (2*a)
  answer2 = ((-b) - (d**0.5)) / (2*a)
  print(f'근은 {answer1}, {answer2} 입니다.')
elif d == 0:
  answer3 = (-b) / (2*a)
  print(f'근은 {answer3} 입니다.') 
else:
  print('허근입니다.')  
```

