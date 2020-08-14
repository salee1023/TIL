# 0729_workshop

### 1. pip 

> 아래 명령어는 (1) 무엇을 위한 명령인지 (2) 실행은 어디에서 해야하는지 작성하시오.

```bash
$ pip install faker
```

- `  pip` (패키지 관리자)

(1) faker이라는 외부 패키지를 설치하도록 도와준다.

(2) 명령 프롬프트 (cmd) (python이 설치되어있는 어디에서나.)



### 2. Basic Usage

> Faker는 다양한 메서드를 통해 임의의 결과값을 반환해준다. 임의의 영문 이름을 반환하는 아래 코드에서 라인별 의미를 주석을 참고하여 작성하시오.

```python
# faker 패키지의 Faker 클래스 추가하기 위한 코드이다. 
from faker import Faker
# Faker는 클래스, fake는 인스턴스 
fake = Faker()
# name()은 fake의 인스턴스 메서드
fake.name()
```



### 3. Localization

> Faker는 다양한 언어의 Locale을 지원한다. 

```python
# 1. 인자 없이 호출 시에는 영문이 기본 설정이다. (en_US)
fake = Faker()
fake.name()

# 2. Locale 정보를 포함하여 호출 시에는 해당 언어 설정을 따른다.
fake = Faker()
fake.name()
```

> 직접 해당하는 기능을 구현한다고 하였을 때, 빈칸 (a), (b), (c)에 들어갈 코드로 적절한 것을 작성하시오. 

```python
class Faker():
    
    def __init__(self, locale = 'en_US'):
 		pass       
```



### 4. Seeding the Generator

> 아래의 코드를 실행 했을 때, #1과 #2에서 출력되는 결과를 각각 작성하고,  seed()는 어떤 종류의 메서드인지 작성하시오. 

```python
fake = Faker('ko_KR')
Faker.seed(4321)
print(fake.name()) # 1 이도윤

fake2 = Faker('ko_KR')
print(fake2.name()) # 2 이지후

fake3 = Faker('ko_KR')
fake3.seed_instance()
print(fake3.name()) # 3 이도윤
```

- `Faker.seed(4321)`  : 클래스 범위에서 seed값을 지정해주기 때문에, 여러 인스턴스를 생성하여 `.name` 을 실행해도 항상 같은 순서, 같은 이름이 출력된다. (이도윤, 이지후, 김광수, 조승민 ...)
- `fake3.seed_instance()`  : 인스턴스에 seed값을 지정해주기 때문에, 항상 같은 이름이 출력된다. (이도윤)



