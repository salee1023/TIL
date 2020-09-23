# 0923_homework

### 1. 1:N True or False

1) ForiegnKey는 부모 테이블의 데이터를 참조하기 위한 키이다. (T)

2) 1:N 관계에서 1은 N의 데이터를 직접 참조 할 수 있다. 

​	(F) 직접 참조 못한다. django의 힘을 빌려 (ex)`comment_set` 와 같이 참조한다.

3) on_delete 속성은 ForeignKey 필드의 필수 인자이다. (T)

4) 1:N 관계에서 ForeignKey는 반드시 부모 테이블의 PrimaryKey여야 한다. 

​	(F) PK일 필요는 없지만, **유일**해야 한다.

---

### 2. ForeignKey column name

> 다음과 같이 이름이 articles인 app의 models.py에 작성된 코드를 바탕으로 테이블이 만들어 졌을 때, 데이터베이스에 저장되는 ForeignKey 컬럼의 이름과 테이블의 이름이 무엇인지 작성하시오.

```python
from django.db import models

class Question(models.Model):
    title = models.CharField(max_length=50)
    
class Comment(models.Model):
    answer = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.CharField(max_length=100)
```

👉 컬럼 : `answer_id`, 테이블 : `articles_comment`

---

### 3. 1:N ORM in template

> 위 2번 문제 모델 관계를 바탕으로 어느 template 페이지가 다음과 같이 작성되어 있을 때, 질문(Question)에 작성된 모든 댓글 (Comment)을 출력하고자 한다. 해당 template에서 Question 객체를 사용할 수 있다면 빈칸에 들어갈 알맞은 코드를 작성하시오.

```html
{% for comment in ___(a)___%}
	<p>{{ comment.content }}</p>
{% endfor %}
```

👉 question.comment_set.all

---

### 4. ?next=

> 다음과 같이 게시글을 삭제하는 delete 함수와 로그인을 위한 login 함수가 작성되어 있다. 만약 비로그인 사용자가 삭제를 시도한다면 django는 해당 사용자를 url에 next 파라미터가 붙은 login 페이지로 redirect한다.

- /accounts/login/?next=/articles/1/delete/

  > redirect된 로그인 페이지에서 로그인에 성공했을 때 발생하는 HTTP response status code를 작성하고 발생한 원인과 해결을 위해 코드를 수정하시오.

```python
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import Article

@login_required
@require_POST
def delete(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    article.delete()
    return redirect('articles:index')
```

```python
def login(request):
    if request.user.is_authenticated:
        return redirect('articles:index')       
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect(request.GET.get('next') or 'articles:index')
    else:
        form = AuthenticationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/login.html', context)
```

👉 로그인을 끝낸  redirect 된 request는 GET method이다. 따라서, 다시 delete로 돌아가면 `@require_POST`로 인해 막히고 `405 Method Not Allowed` 에러를 발생시킨다.

👉 `@require_POST` 를 없애고, delete안에서  `if request.method == 'POST'` 조건을 추가하여 해결한다.

