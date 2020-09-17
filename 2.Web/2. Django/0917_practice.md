# 1. User Create

> /accouts/signup/ 회원가입 기능을 구현한다.

```python
# views.py

from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, PasswordChangeForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.contrib.auth import get_user_model
from .forms import CustomUserChangeForm

# CREATE -> Session 정보를 생성
def login(request):
    # 이미 로그인되어 있다면 articles/index로 이동
    if request.user.is_authenticated:
        return redirect('articles:index')

    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        # 사용자가 입력한 ID와 PW 유효성 검사
        if form.is_valid():
            # 로그인을 하기 위해, 로그인 함수에 request 정보와, 사용자 인스턴스를 넘겨준다.
            # 장고가 개발자가 쿠키와 세션 구현에 대해 신경쓰지 않고, 편하게 로그인 기능을 개발할 수 있도록 제공한 함수
            auth_login(request, form.get_user())
            # redirect -> 'GET'요청으로 처리됨
            return redirect(request.GET.get('next') or 'articles:index')
    else:
        form = AuthenticationForm()
    context = {
        'form': form,
    }    
    return render(request, 'accounts/login.html', context)


@login_required
def update(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('articles:index')
    else:
        form = CustomUserChangeForm(instance=request.user)
    context = {
        'form': form,
    }
    return render(request, 'accounts/update.html', context)


# DELETE Session 
def logout(request):
    auth_logout(request)
    return redirect('articles:index')




# 만약 @login_required 데코레이터를 사용하면, 위에 login 함수로 들어가서 로그인을 한 뒤 next의 GET요청으로 들어옴
# 그러면 require_POST에 한번 더 걸리면서 delete가 실행이 안됨.
# 따라서 POST를 먼저 확인하고, 로그인이 되어 있다면, delete한다. 애초에 base.html에서 로그인 되어있을때만 탈퇴버튼이 뜨도록 만들었기 때문에,
# 상관없음.


# DELETE user
@require_POST
def delete(request):
    if request.user.is_authenticated:
        request.user.delete()
        return redirect('articles:index')


@login_required
def password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            # 비밀번호를 변경해도 세션유지로 로그인 상태 유지
            update_session_auth_hash(request, user)
        return redirect('articles:index')
    else:
        form = PasswordChangeForm(request.user)
    context = {
        'form': form,
    }
    return render(request, 'accounts/password.html', context)

```

![image-20200917191238432](0917_practice.assets/image-20200917191238432.png)

```html
{% extends 'base.html' %}
{% load static %}

{% block content %}
  <div class="d-flex justify-content-between">
    <img src="{% static 'articles/images/cat.jpg' %}" alt="cat">
    <img src="{% static 'articles/images/cat.jpg' %}" alt="cat">
    <img src="{% static 'articles/images/cat.jpg' %}" alt="cat">
  </div>
  <hr>
  <h1>Articles</h1>
  {% if request.user.is_authenticated %}
    <a href="{% url 'articles:create' %}">NEW</a>
  {% else %}
    <a href="">[새 글을 작성하려면 로그인 하세요!]</a>
  {% endif %}
  <hr>
  {% for article in articles %}
    <h2>{{ article.pk }}</h2>
    <h2>{{ article.title }}</h2>
    <a href="{% url 'articles:detail' article.pk %}">[detail]</a>
    <hr>
  {% endfor %}
{% endblock %}
```

---

### 👉 회원 목록 기능 구현

![image-20200917191939723](0917_practice.assets/image-20200917191939723.png)

```python
# urls.py
from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    path('', views.index, name='index'),
]
```

```python
# views.py
User = get_user_model()

def index(request):
    users = User.objects.all()
    context = {
        'users': users,
    }
    return render(request, 'accounts/index.html', context)
```

---

### 👉 비밀번호 수정 기능

![image-20200917192415599](0917_practice.assets/image-20200917192415599.png)

password 암호화 알고리즘 & 해쉬값

```
알고리즘: PBKDF2 
해쉬: SHA256 
```

