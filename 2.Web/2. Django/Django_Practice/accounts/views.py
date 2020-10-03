from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST, require_http_methods
from django.contrib.auth import get_user_model
from .forms import CustomUserChangeForm, CustomUserCreationForm

# User모델에는 직접적으로 접근할 수 없다.
User = get_user_model()

def index(request):
    users = User.objects.all()
    context = {
        'users': users,
    }
    return render(request, 'accounts/index.html', context)


# CREATE -> Database에 회원데이터를 생성
@require_http_methods(['GET', 'POST'])
def signup(request):
    # 이미 로그인이 되어있다면, articles/index로 이동
    if request.user.is_authenticated: 
        return redirect('articles:index')

    if request.method =='POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            # 회원가입 폼의 데이터를 DB에 저장하는 코드를 user라는 변수에 저장
            user = form.save()
            # 회원 DB 저장한 뒤 자동 로그인 코드
            auth_login(request, user)
            return redirect('articles:index')
    else:
        form = CustomUserCreationForm()
    context = {
        'form': form,
    }    
    return render(request, 'accounts/signup.html', context)


@require_http_methods(['GET', 'POST'])
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
@require_http_methods(['GET', 'POST'])
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
# 따라서 POST를 먼저 확인하고, 로그인이 되어 있다면, delete한다. 애초에 base.html에서 로그인 되어있을때만 탈퇴버튼이 뜨도록 만들었기 때문에,상관없음.


# DELETE user
@require_POST
def delete(request):
    if request.user.is_authenticated:
        request.user.delete()
        return redirect('articles:index')


@login_required
@require_http_methods(['GET', 'POST'])
def change_password(request):
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
    return render(request, 'accounts/change_password.html', context)


def profile(request, username):
    person = get_object_or_404(get_user_model(), username=username)
    context = {
        'person': person,
    }
    return render(request, 'accounts/profile.html', context)


@require_POST
@login_required
def follow(request, user_pk):
    you = get_object_or_404(get_user_model(), pk=user_pk)
    me = request.user

    if me != you:
        if you.followers.filter(pk=me.pk).exists():
            you.followers.remove(me)
        else:
            you.followers.add(me)
    return redirect('accounts:profile', you.username)


