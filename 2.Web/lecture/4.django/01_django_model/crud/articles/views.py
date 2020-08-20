from django.shortcuts import render, redirect
from .models import Article


# [GET] 게시글 전체 리스트를 보여주는 함수
def index(request):
    # 1. ARticle 모델 클래스의 모든 인스턴스 들고오기 -> 리턴 값은 퀴리셋 형태
    articles = Article.objects.order_by('-pk') #DB단
    # articles = Article.objects.all()[::-1] #python단
    context = {
        'articles' : articles,
    }
    return render(request, 'articles/index.html', context)


# [GET] 게시글 하나에 대한 상세정보를 보여주는 함수
def detail(requests, pk):
    article = Article.objects.get(pk=pk)
    context = {
        'article' : article,
    }
    return render(requests, 'articles/detail.html', context)


# [GET] 사용자에게 게시글 작성 Form을 보여주는 함수
def new(request):
    return render(request, 'articles/new.html')


# [POST] 사용자로부터 Form으로 제출한 데이터를 받아서 DB에 저장하는 함수
def create(request):
    # 1. DB 저장하기
    # 1-1. 사용자가 제출한 데이터 추출하기
    title = request.POST.get('title')
    content = request.POST.get('content')

    # 1-2. DB에 새로운 게시글 저장하기
    # article = Article(title=title, content=content)
    # article.save()
    article = Article.objects.create(title=title, content=content)

    # 2. DB 저장이 끝난 후 게시글 상세정보로 리다이렉트하기
    # return render(request, 'articles/create.html')    
    # return render(request, 'articles/index.html')    
    # return redirect('/articles/') 
    # return redirect('articles:index')
    return redirect('articles:detail', article.pk)


def delete(request, pk):
    # 요청 형태가 'POST'인 경우에만 게시글 삭제
    # 1. 삭제할 게시글 가져오기
    article = Article.objects.get(pk=pk)
    if request.method =='POST':
        # 2. 삭제하기
        article.delete()
        # 3. 메인 페이지로 Redirect
        return redirect('articles:index')
    # 'POST'가 아니면
    else:
        return redirect('articles:index', article.pk)


def edit(request, pk):
    article = Article.objects.get(pk=pk)
    context = {
        'article' : article,
    }
    return render(request, 'articles/edit.html', context)


def update(request, pk):
    # 1. 수정할 pk번 게시글 가져오기
    article = Article.objects.get(pk=pk)

    # 2. 사용자가 제출한 데이터로 게시글 정보 수정하기
    article.title = request.POST.get('title')
    article.content= request.POST.get('content')
    
    # 3. 데이터베이스에 저장하기
    article.save()
    
    # 4. 게시글 상세정보 페이지로 Redirect 
    return redirect('articles:detail', article.pk)