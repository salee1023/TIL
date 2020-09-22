# 0921_homework

#### 1. Lookup

> 지문의 코드에서 '__gt' 부분을 lookup이라고 한다. 링크를 참고하여 Django에서 사용가능 한 lookup 세가지와 그 의미를 작성하시오.

```python
Entry.objects.filter(pk__gt=4)
```

`__gt` : greater than (초과)

`__gte` : greater than or equal to (이상)

`__lt`: less than (미만)

`__lte` : less than or equal to (이하)

---

#### 2. 1:N 관계 설정 

> 지문은 1:N 관계 설정을 하기 위하여 정의된 모델이다. 링크를 참고하여 빈 칸에 들어갈 수 있는 값 세가지와 그 의미를 작성하시오.

```python
class Comment(models.Model):
    content = models.CharField(max_length=100)
    article = models.ForeignKey(Article, on_delete=(___(a)__))
```

👉 ForeignKey가 가리키는 데이터가 삭제되었을 때,  해당 데이터를 어떻게 처리할 지를 선택한다.

`models.CASCADE` :  ForeignKey를 들고있는 본 데이터도 함께 삭제한다.

`models.PROTECT` :  ForeignKey가 가리키는 데이터가 삭제되기전, 에러를 먼저 발생시킨다.

`models.RESTRICT` : ForeignKey가 가리키는 데이터가 함께 삭제되는 경우 삭제하고,  남아있는 경우면 에러를 								발생시킨다.

`models.SET_NULL` : ForeignKey값을 null로 바꾼다

`models.SET_DEFAULT` : ForeignKey를 default 값으로 바꾼다.

`models.DO_NOTHING` : 아무런 행동을 하지 않는다. (위험!!)

---

#### 3. comment create

> 지문은 댓글 기능을 작성하기 위한 코드이다. 빈 칸에 들어갈 코드를 작성하시오.

```python
def comments_create(request, pk):
        article = Article.objects.get(pk=pk)
        if request.method == 'POST':
            form = CommentForm(request.POST)
        	if comment_form.is_valid():
           		comment = comment_form.save(___(a)___)
            	comment.article = article
            	comment.save()
            	return redirect('articles:index')
```

(a) : commit=False

---

#### 4. 1:N ORM

> 게시물 아래에 댓글을 출력하려고 한다. post와 comment 모델이 1:N으로 관계설정이 되어 있다고 가정 할 때 아래의 빈칸에 적절한 코드를 작성하시오.

```html
<h1>{{ article.title }}</h1>
{% for comment in __(a)__%}
	<p>{{ comment.content }}</p>
{% empty %}
	<p>댓글이 없습니다.</p>
{% endfor %}
```

(a) : comments