from django.shortcuts import render, redirect
from .models import Article

# 초기 화면
def index(request):
    articles = Article.objects.all()
    context = {
        'articles' : articles,
    }
    return render(request, 'articles/index.html', context)


# 폼으로 ㄱㄱ 
def new(request):
    return render(request, 'articles/new.html')


# 폼의 데이터를 DB에 저장
def create(request):
    title = request.POST.get('title')
    content = request.POST.get('content')
    article = Article.objects.create(title=title, content=content)
    return redirect('articles:detail', article.pk)


# 게시물 상세페이지
def detail(request, pk):
    article = Article.objects.get(pk=pk)
    context = {
        'article' : article,
    }
    return render(request,'articles/detail.html', context)


def edit(request, pk):
    article = Article.objects.get(pk=pk)
    context = {
        'article' : article
    }
    return render(request,'articles/edit.html', context)


def update(request, pk):
    article = Article.objects.get(pk=pk)
    article.title = request.POST.get('title')
    article.content = request.POST.get('content')
    article.save()
    return redirect('articles:detail', article.pk)    


def delete(request, pk):
    article = Article.objects.get(pk=pk)
    article.delete()
    return redirect('articles:index')
      