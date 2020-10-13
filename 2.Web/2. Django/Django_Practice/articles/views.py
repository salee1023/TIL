from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST, require_http_methods
from django.contrib.auth.decorators import login_required
from .models import Article, Comment
from .forms import ArticleForm, CommentForm

# Create your views here.
def index(request):
    # articles = Article.objects.all()
    articles = Article.objects.order_by('-pk')
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)

# def new(request):
#     form = ArticleForm()
#     context = {
#         'form': form,
#     }
#     return render(request, 'articles/new.html', context)



# def create(request):
#     title = request.POST.get('title') 
#     content = request.POST.get('content')
#     article = Article(title=title, content=content)
#     article.save()
#     return redirect('articles:detail', article.pk)

@login_required
@require_http_methods(["GET", "POST"])
def create(request):
    # http method가 POST 일 때
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)
        # 유효성 검증
        if form.is_valid():
            article = form.save(commit=False)
            article.user = request.user
            article.save()
            return redirect('articles:detail', article.pk)
    # http method가 POST가 아닌 다른 method 일 때
    else: # new
        form = ArticleForm()
    context = {
        # 1. is_valid에서 내려온 form : 에러메세지를 포함
        # 2. else 구문에서 내려온 form 
        'form': form,
    }
    return render(request, 'articles/create.html', context)


@require_POST
def comments_create(request, pk):
    if request.user.is_authenticated:
        article = Article.objects.get(pk=pk)
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.article = article
            comment.user = request.user
            comment.save()
            return redirect('articles:detail', article.pk)
        context = {
            'article': article,
            'comment_form': comment_form
        }    
        return render(request, 'articles/detail.html', context)
    return redirect('accounts:login')


def detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    comment_form = CommentForm()
    context = {
        'article': article,
        'comment_form': comment_form,
    }
    return render(request, 'articles/detail.html', context)


@login_required
@require_http_methods(["GET", "POST"])
def update(request, pk):
    article = get_object_or_404(Article, pk=pk)
    # 수정하는 유저와, 게시글 작성 유저가 같으면
    if request.user == article.user:
        if request.method == 'POST': # update
            # Create a form to edit an existing Article, but use POST data to populate the form.
            form = ArticleForm(request.POST, request.FILES, instance=article)
            if form.is_valid():
                form.save()
                return redirect('articles:detail', article.pk)
        else: # edit
            # Creating a form to change an existing article.
            form = ArticleForm(instance=article)
        context = {
            'form': form,
            'article': article,
        }
        return render(request, 'articles/update.html', context)
    return redirect('articles:detail', article.pk)


@require_POST
def delete(request, review_pk):
    article = Article.objects.get(pk=review_pk)
    article.delete()
    return redirect('articles:index')    


@require_POST
def comments_delete(request, article_pk, comment_pk):
    if request.user.is_authenticated:
        comment = get_object_or_404(Comment, pk=comment_pk)
        if request.user == comment.user:
            comment.delete()
    return redirect('articles:detail', article_pk)


@require_POST
def like(request, article_pk):
    if request.user.is_authenticated:
        article = get_object_or_404(Article, pk=article_pk)
        # user가 article에 좋아요를 눌렀는지 안눌렀는지 판단
        # 1-1. user가 article을 좋아요 누른 유저리스트에 in 인지
        # if request.user in article.like_user.all():
        #     article.like_users.remove(request.user)
        # 1-2. user가 article을 좋아요 누른 전체유저에 exist하는지
        if article.like_users.filter(pk=request.user.pk).exists():
            article.like_users.remove(request.user)
        else:
            article.like_users.add(request.user)
        return redirect('articles:index')
    return redirect('accounts:login')

