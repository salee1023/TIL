# 💻 PJT 04

## 1. 프로젝트 주제

영화 커뮤니티 서비스 게시판 기능 개발 (Django Form 활용)

<br>

## 2. 프로젝트 목표 

- 데이터를 생성, 조회 할 수 있는 Web Application 제작
- Python Web Framework를 통한 데이터 조작
- Object Relational Mapping에 대한 이해
- django ModelForm을 활용한 HTML과 사용자 요청 데이터 관리

<br>

## 3. 준비사항

- 언어
  -  Python 3.7+
  -  Django 3.X
- 도구
  -  vsCode
  -  Chrome Browser

<br>

## 4. 프로젝트 진행과정

### 4-0. 모델 생성

```python
# models.py

from django.db import models

# Create your models here.
class Review(models.Model):
    title = models.CharField(max_length=100) 
    movie_title = models.CharField(max_length=50) 
    content = models.TextField() 
    rank = models.IntegerField() 
    created_at = models.DateTimeField(auto_now_add=True) 
    updated_at = models.DateTimeField(auto_now=True) 
    
    # admin계정에서 review 타이틀이 보이도록 설정
    def __str__(self):
        return self.title
```

```python
# forms.py
from django import forms
from .models import Review

class ReviewForm(forms.ModelForm):

    class Meta:
        model = Review
        fields = '__all__'
```

👉 Review의 데이터 검증, 저장, 에러메시지, HTML을 종합적으로 관리하기 위해 ModelForm을 사용한다.

👉 `fields = '__all__'` 로 Model의 모든 필드를 가져온다. (created_at와 updated_at은 자동으로 생성된다.)

```bash
$ python manage.py createsuperuser
```

👉 admin 계정을 생성하여 테스트를 용이하게 만들어 준다.

<br>

---

<br>

### 4-1. CRUD

- **urls.py, views.py**

✔ Review **Create, Read, Update, Delete** 기능 구현

```python
# urls.py

from django.urls import path
from . import views
app_name = 'community'
urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('<int:pk>/', views.detail, name='detail'),
    path('<int:pk>/update/', views.update, name='update'),
    path('<int:pk>/delete/', views.delete, name='delete'),
]
```

```python
# views.py

from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods, require_POST
from .models import Review
from .forms import ReviewForm

def index(request):
    reviews = Review.objects.order_by('-pk')
    context = {
        'reviews': reviews,
    }
    return render(request, 'community/review_list.html', context)

@require_http_methods(["GET", "POST"])
def create(request):
    # http method가 POST 일 때
    if request.method == 'POST':
        form = ReviewForm(request.POST, request.FILES)
        # 유효성 검증
        if form.is_valid():
            review = form.save()
            return redirect('community:detail', review.pk)
    else: # new
        form = ReviewForm()
    context = {
        'form': form,
    }
    return render(request, 'community/create.html', context)


def detail(request, pk):
    review = Review.objects.get(pk=pk)
    context = {
        'review': review,
    }
    return render(request, 'community/review_detail.html', context)


@require_http_methods(["GET", "POST"])
def update(request, pk):
    review = Review.objects.get(pk=pk)
    if request.method == 'POST':
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            return redirect('community:detail', review.pk)
    else:
        form = ReviewForm(instance=review)
    context = {
        'form': form,
        'review': review,
    }
    return render(request, 'community/update.html', context)


@require_POST
def delete(request, pk):
    review = Review.objects.get(pk=pk)
    review.delete()
    return redirect('community:index')
```

- **CREATE**

![image-20200918174203758](README.assets/image-20200918174203758.png)



- **READ**

![image-20200918173943929](README.assets/image-20200918173943929.png)

![image-20200918174346124](README.assets/image-20200918174346124.png)

- **UPDATE**

![image-20200918174402149](README.assets/image-20200918174402149.png)

- **DELETE**

(구현 화면 x)

<br>

----

<br>

###  4-2. HTML

- **base.html**

✔  CRUD에 사용되는 각 페이지는 base.html을 확장하여 사용한다.

✔  base.html 상단에 navbar을 만들어 리뷰 목록 조회와 새로운 리뷰 작성 페이지로 이동 할 수 있게 한다.

```html
<nav class="navbar navbar-expand-lg navbar-dark bg-dark fixed-top">
        <a class="navbar-brand" href="#">COMMUNITY</a>
    <div class="justify-content-end collapse navbar-collapse" id="navbarNav">
        <ul class="navbar-nav mx-3">
        <li class="nav-item mx-1">
            <a class="nav-link" href="{% url 'community:index' %}">HOME</a>
        </li>
        <li class="nav-item mx-1">
            <a class="nav-link" href="{% url 'community:create' %}">NEW</a>
        </li>
        </ul>
    </div>
</nav>
```

```html
{% extends 'base.html' %}
{% block content %}
  <h1 class="text-center">CREATE</h1>
  <form action="" method="POST">
    {% csrf_token %}
    {{ form.as_p }}
    <input type="submit">
  </form>
{% endblock %}
```

👉 각 페이지는 `base.html`과 만든 `modelform`을 사용한다.

![image-20200918173943929](README.assets/image-20200918173943929.png)

<br>

---

<br>

### 4-3. Pair Project

- **Trello**

✔  명세서 기반으로 To-Do List를 작성하고,  진행상황을 파악하기에 용이하다.

![image-20200918175241153](README.assets/image-20200918175241153.png)



- **LIVE SHARE**

✔  Webex를 사용하기 어려웠을 때, 화면 공유를 위해  vscode extensions에서 LIVE SHARE를 활용

<br>

----



### 5. 정리

😉 Webex, Mattermost, Gitlab, Trello, LIVE SHARE등 다양한 협업툴을 활용할 수 있었다.

😉 페어와 함께 CRUD 구현 과정을 다시한번 복습할 수 있었다.

😉 데코레이터의 소중함을 알게되었다.

🤢 기능을 구현할 때 구현 순서에 유의하여 에러를 줄여야겠다.

✨  부트스트랩으로 디자인 개선하기

✨ 다음엔 협업툴의 더욱 다양한 기능을 활용해보자!

