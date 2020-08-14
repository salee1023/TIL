# 0814_homework

### 1. settings

django 서버를 실행하고 첫 페이지에 접속했을 때 터미널에 출력된 서버 시간이 현재 한국 시간과 다른 시간으로 출력된다. 이를 한국 시간으로 바꾸려면 settings.py의 어떤 변수에 어떤 값을 할당해야 하는지 작성하시오.

```python
TIME_ZONE = 'Asia/Seoul'
```



---



### 2. urls

 다음은 어떤 django 프로젝트의 urls.py의 모습이다. 주소 '/ssafy'로 요청이 들어왔을 때 실행되는 함수가 pages앱의 views.py 파일 안 ssafy 함수라면, 요청에 응답하기 위해 빈칸 (a)에 추가되어야 할 코드를 작성하시오.

```python
from django.contrib import admin
from django.urls import path
from pages import views

urlpatterns = [
    path(__(a)__),
    path('admin/', admin.site.urls),
]
```

```python
path('ssafy/', views.ssafy)
```



---



### 3. Django Template Language

1) menus 리스트를 반복문으로 출력하시오.

```html
{% for menu in menus %}
	<p>{{ menu }}</p>
{% endfor %}
```



2) posts 리스트를 반복문을 활용하여 0번 글부터 출력하시오.

```html
{% for post in posts %}
	<p>{{ forloop.counter }}번 글 : {{ post }}</p>
{% endfor %}
```



3) users 리스트가 비어있다면 **현재 가입한 유저가 없습니다.** 텍스트를 출력하시오.

```html
{% for user in users %}
	<p>{{ user }}</p>
{% empty %}
	<p>현재 가입한 유저가 없습니다.</p>
{% endfor %}
```



4) 첫 번째 반복문일 때와 아닐 때를 조건문으로 분기처리 하시오.

```html
{% if forloop.first %}
	<p>첫 번째 반복문 입니다.</p>
{% else %}
	<p>첫 번째 반복문이 아닙니다.</p>
{% endif %}
```



5) 출력된 결과가 주석과 같아지도록 하시오.

```html
<!-- 5 -->
<p>{{ 'hello'|length}}</p>
<!-- My Name Is Tom -->
<p>{{ 'my name is tom'|capfirst}}</p>
```



6) 변수 today에 datetime 객체가 들어있을 때 출력된 결과가 주석과 같아지도록 하시오.

```html
<!-- 2020년 02월 02일 (Sun) PM 02:02 -->
{{today|date:"o년 m월 d일 (D) A H:i"}}
```



---

### 4. Form tag

다음은 form tag에 관한 문제이다. 올바른 답을 작성하시오.

**1) 지문의 코드 중 form 태그의 속성인 action의 역할에 대해 설명하시오.**

`action` : 폼 데이터를 서버로 보낼 때, 해당 데이터가 도착할 URL을 명시한다.

**2) 지문의 코드 중 method가 가질 수 있는 속성 값을 작성하시오.**

`GET` `POST` 

**3) input 태그에 각각 '안녕하세요' , '반갑습니다' , '파이팅' 문자열을 넣고 submit 버튼을 눌렀을 때 이동하는 ul경로를 작성하시오.**

?title=안녕하세요&content=반갑습니다&my-site=파이팅
