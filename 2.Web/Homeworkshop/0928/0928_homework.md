# 0928_homework

### 1. MTV

> Django는 MTV로 이루어진 Web Framework다. MTV가 무엇의 약자이며 Django에서 각각 어떤 역할을 하고 있는지 작성하시오.

M (Model) : 데이터를 처리하는 로직이다. 

T (Templates) : 사용자의 요청에 따른 데이터를 사용자에게 보여준다.

V (View) : Model과 Templates 사이를 이어주는 로직이다.

---

### 2. 404 Page not found

> '/' 페이지에 접속했을 때 articles의 index.html을 렌더링 하기 위해서 작성해야 하는 알맞은 코드를 작성하시오.

```python
from django.contrib import admin
from django.urls import path, include
from __(a)__ import __(b)__

urlpatterns = [
    path('admin/', admin.site.urls),
    path('articles/', include('articles.urls')),
    path('', __(c)__),
]
```

(a) : `articles`

(b) : `views`

(c) : `views.index`

---

### 3. templates and static

> Django 프로젝트는 기본적으로 render 할 html과 같은 template 파일과 css, js와 같은 static파일을 앱 폴더 내부에서 찾는다. 만약 해당 위치가 아닌 임의의 위치에 파일을 위치 시키고 싶으면 `__(a)__` 파일의 `__(b)__` 과 `__(c)__` 라는 변수에 담긴 리스트의 요소를 수정하면 된다. 

(a) : `settings.py`

(b) : `TEMPLATES` 의 `'DIRS'`

(c) : `STATICFILES_DIRS`

---

### 4. migration

1) 마이그레이션 생성 : `python manage.py makemigrations`

2) 마이그레이션 DB 반영 여부 확인 : `python manage.py showmigrations`

3) 마이그레이션에 대응되는 SQL문 출력 : `python manage.py sqlmigrate app_name xxxx`

4) 마이그레이션 파일의 내용을 DB에 최종 반영 : `python manage.py migrate`

---

### 5. ModelForm True or False

1) POST 와 GET 방식은 의미론상의 차이이며 실제 동작 방식은 동일하다. (F)

2) ModelForm과 Form Class의 핵심 차이는 Model의 정보를 알고 있는지의 여부이다. (T)

3) AuthenticationForm 은 User 모델과 관련된 정보를 이미 알고 있는 ModelForm으로 구성되어 있다. (F)

4) ModelForm을 사용할 때 Meta 클래스에 fields 관련 옵션은 반드시 작성해야 한다. (T)

