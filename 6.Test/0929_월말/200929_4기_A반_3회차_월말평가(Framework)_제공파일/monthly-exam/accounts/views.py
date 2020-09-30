from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.forms import (
    UserCreationForm,
    AuthenticationForm,
)
from django.contrib.auth.decorators import login_required


# Create your views here.
def signup(request):
    # Q1-1
    # 로그인 한 유저의 경우 /reservations/경로로 redirect한다.
    if request.user.is_authenticated:
        return redirect('reservations:index')
    # POST 요청 시 사용자 정보 저장
    if request.method == "POST": 
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('reservations:index')     
    # GET 요청 시 회원가입
    else: 
        form = UserCreationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/signup.html', context)
    
    
def login(request):
    # Q1-2
    # 로그인 한 유저의 경우 /reservations/경로로 redirect
    if request.user.is_authenticated:
        return redirect('reservations:index')

    # POST 요청 시 세션에 로그인 정보 저장
    if request.method == "POST": 
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('reservations:index')     
    # GET 요청 시 로그인
    else: 
        form = AuthenticationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/login.html', context)
  
    
@login_required
def logout(request):
    # Q1-3
    auth_logout(request)
    return redirect('accounts:login')
    