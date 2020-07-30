# 0729_homework

### 1. Type Class

> Python은 객체 지향 프로그래밍 언어이다. Python에서 기본적으로 정의되어 있는 클래스를 최소 5가지 이상 작성하시오. 

int, float, str, list, dict





### 2. Magic Method

> 아래에 제시된 매직 메서드들이 각각 어떠한 역할을 하는지 간단하게 작성하시오.

- `__init__`  :  인스턴스 객체가 생성될 때 호출된다. `__init__`으로 인스턴스의 속성을 정의할 수 있다.

- `__del__  ` : 인스턴스 객체가 사라지기 직전에 호출되는 함수이다. 

- `__str__`  : 인스턴스를 print()로 출력 할 때 사용한다. 디버깅할 때 유용하게 사용한다.

- `__repr__` : 시스템이 해당 객체를 인식할 수 있는 공식적인 문자열 형태로 반환할 때 사용한다. 

  `__str__ ` 과`__repr__`의 차이점

  ```python
  class Person:
      
      def __init__(self, name, age):
          self.name = name
          self.age = age
  
      def __str__(self):
          return f'이름은 : {self.name} , 나이는 : {self.age}'
  
      def __repr__(self):
          return f'<Person: {self.name}>'
  
  p1 = Person('승아', 25)
  
  print(p1) #1
  p1 #2
  ```

  ```
  #1
  이름은 : 승아 , 나이는 : 25 
  #2
  <Person: 승아> 
  ```

  

  

### 3. Instance Method

> .sort()와 같이 문자열, 리스트, 딕셔너리 등을 조작할 때, 사용하였더던 것들은 클래스에 정의된 메서드들이었다. 이처럼 문자열, 리스트, 딕셔너리 등을 조작하는 메서드를 최소 3가지 이상 그 역할과 함께 작성하시오.

`.append(x)` : 리스트의 끝에 항목을 더한다.

`.clear()` : 리스트의 모든 항목을 삭제한다.

`.count(x) ` : 리스트에서 x가 등장하는 횟수를 돌려준다.  

`.extend(iterable)` : 리스트 끝에 iterable한 모든 항목을 덧붙여서 확장한다.

`.insert(i,x)` : 주어진 위치에 항목을 삽입한다. 

 

### 4. Module Import

>  아래와 같은 코드가 같은 폴더 안에 fibo.py 파일에 작성되어 있을 때, 함수를 실행할 수 있는 import 문을 작성하시오.

```python
# fibo.py
def fibo_recursion(n):
    if n < 2:
        return n
    else:
        return fibo_recursion(n-1) + fibo_recursion(n
```

```python
from fibo import fibo_recursion as recursion
recursion(4)
```







