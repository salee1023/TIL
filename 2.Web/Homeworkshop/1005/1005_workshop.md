# 1005_workshop

### 1. Model & Admin

> Article
>
> - title, content, created_at, updated_at 컬럼이 존재한다.
> - 관리자 페이지를 활용하여 5개의 게시글을 생성한다.

```python
# models.py
from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.title}'
```

---

### 2. serializers

> ArticleListSerializer
>
> - 모든 게시글 정보를 반환하기 위한 Serializer
> - id, title 필드 정의
>
> ArticleSerializer
>
> - 상세 게시글 정보를 반환 및 생성하기 위한 Serializer
> - id, title, content, created_at, updated_at 필드 정의

```python
# serializers.py
from rest_framework import serializers
from .models import Article, Comment

class ArticleListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Article
        fields = ['id', 'title',]
        

class ArticleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Article
        fields = '__all__'    
```

---

### 3. url & views

> **GET** api/v1/articles/
>
> - 모든 게시글의 id와 title 컬럼을 JSON으로 응답한다.
>
> **POST**  api/v1/articles/
>
> - 검증에 성공하는 경우 새로운 게시글의 정보를 DB에 저장하고 저장된 게시글의 정보를 응답한다.
> - 검증에 실패하는 경우 400 Bad Request 오류를 발생시킨다.
>
> **GET** api/v1/articles/<article_pk>/
>
> - 특정 게시글의 모든 컬럼을 JSON으로 응답한다.
>
> PUT & DELETE api/v1/articles/<article_pk>
>
> - PUT 요청인 경우 특정 게시글의 정보를 수정한다.
> - DELETE 요청인 경우 특정 게시글의 정보를 삭제한다.

```python
@api_view(['GET', 'POST'])
def article_list_create(request):
    if request.method == 'GET':
        articles = Article.objects.all()
        serializer = ArticleListSerializer(articles, many=True)
    else:
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
    
    return Response(serializer.data)


@api_view(['GET', 'PUT', 'DELETE'])
def article_detail_update_delete(request, article_pk):
    # 조회, 수정, 삭제할 데이터 가져오기 
    # article = Article.objects.get(pk=article_pk)
    article = get_object_or_404(Article, pk=article_pk)

    if request.method == 'GET':
        serializer = ArticleSerializer(article)  # 포맷 변환
        # print(serializer.data)
        # print(type(serializer))
        return Response(serializer.data)  # 응답
    elif request.method == 'PUT':
        # 수정할 인스턴스, 사용자가 요청 보낸 데이터 넣어주기
        serializer = ArticleSerializer(instance=article, data=request.data)  
        # 유효성 검사 후 이상 없으면 저장
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)  # 수정된 데이터 응답
    else:
        # 삭제하기
        article.delete()
        # 메시지 응답
        return Response({'message': f'{article_pk}번 글이 정상적으로 삭제되었습니다.'})
```