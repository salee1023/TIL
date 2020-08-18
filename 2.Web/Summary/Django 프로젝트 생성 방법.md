- Django 프로젝트 생성 방법

```bash
# 새로운 폴더를 만든 뒤, 그 안에 프로젝트 폴더와 manage.py를 생성한다.
$django-admin startproject 프로젝트이름

# 현재 경로에서 프로젝트 폴더와 manage.py를 생성한다.
$django-admin startproject 프로젝트이름 .
```

```
0814/
	first_project/  --최상위 디렉토리명은 자유롭게 바꿀 수 있다.
		first_project/ --실제 프로젝트 폴더명은 바꾸면 안된다.
		manage.py
```

```
movie_project/ --최상위 디렉토리명은 자유롭게 바꿀 수 있다.
	movie_project/
	manage.py
```



- 서버 실행 확인
  - 명령어를 실행하는 경로가 `manage.py` 가 있는 지 확인한다.

```bash
$ python manage.py runserver
```



- Django 애플리케이션 생성
  - 명령어를 실행하는 경로가 `manage.py` 가 있는 지 확인한다.

```bash
$ python manage.py startapp 애플리케이션이름
```



- settings.py

```
1. settings.py에 있는 INSTALLED_APPS 맨 위에 애플리케이션 이름 추가
2. LANGUAGE_CODE ko-kr로 수정 
3. TIME_ZONE 'Asia/Seoul'로 수정
```



- 장고로 만들어진 웹 애플리케이션이라고 생각해보자!
  - [사용자] 사용자는 URL을 통해 특정한 서버 주소를 입력하여 엔터를 누른다! 요청(Request)
  - [장고] 사용자가 요청한 URL을 분석하여 적절한 기능을 연결시켜준다.  `urls.py`
    - 기능을 실행하여 데이터를 가공한 뒤 사용자에게 화면을 렌더링해준다. `views.py`
    - 사용자에게 보여줄 화면은 `templates` 폴더 안에 위치시킨다.

```
path('index/', views.index),
views.py에 
def index(request): 로 만들기
	return render(request, 'index.html')
```





은행 : Django로 만들어진 서비스

고객: 사용자

고객이 어떤 업무를 하고 싶다고 말하면, 몇 번 창구 앞으로 가라고 말하기 `urls.py`

몇 번 창구가 실제로 수행하는 기능들에 대해서 정의하기 `views.py`

5만원 현금을 손으로 건네주는게 아니라 예쁜 봉투에 담아서 건네주기 각 앱에 있는 `templates` 폴더 안의 html 파일

키오스크에서 '대출'버튼 누르기 == 사용자가 브라우저 URL 입력하고 엔터 누르기

직원 안내에 따라 대출 창구로 이동하기  == urls.py-path('대출/', views.대출창구)

5만원 출금 신청하고 5만원 받기 == views.py -def 대출 (request):~

5만원을 예쁜 봉투에 담아서 건네주기  == 템플릿 HTML 코드에 예쁘게 담아서 사용자에게 돌려주기

---



# Django Template Language (DTL)

- django template system 에서 사용하는 built-in-template sysytem이다.
- 조건, 반복, 치환, 필터, 변수 등의 기능을 제공한다.
- 프로그래밍적 로직이 아니라 프레젠테이션을 표현하기 위한 것이다.

- 파이썬처럼 if, for 를 사용할 수 있지만, 이거는 단순히 python code로 실행되는 것이 아니다.

  

syntax

- variable : `{{ }}`
- filters :  `{{ variable|filter}}`

- tags : `{% tag %}`

---

## 템플릿 시스템 설계 철학

- django는 템플릿 시스템이 표현을 제어하는 도구이자 표현에 관련된 로직일 뿐이라고 생각한다.
- 템플릿 시스템에서는 이러한 기본 목표를 넘어서는 기능을 지원해서는 안된다.

for tag

{% for _ in _%}

​	{{ }}

{% endfor %}

 {{ forloop.counter }} : {{ menu }}

