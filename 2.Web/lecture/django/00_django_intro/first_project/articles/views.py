# django imports style guide
# 1. standard library
# 2. 3rd party
# 3. Django
# 4. local django
import random
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')


def dinner(request):
    menus = ['족발','햄버거','치킨','초밥']
    pick = random.choice(menus)
    context = {
        'pick': pick
    }
    return render(request, 'dinner.html', context)


def hello(request, name):
    context = {
        'name' : name,
    }
    return render(request, 'hello.html', context)


def dtl_practice(request):
    menus = ['짜장면', '탕수육', '짬뽕']
    empty_list = []

    context = {
        'menus' : menus,
        'empty_list' : empty_list,
    }
    return render(request, 'dtl_practice.html', context)


def throw(request):
    return render(request, 'throw.html')


def catch(request):
    # throw에서 보낸 form 데이터를(request.GET)을 받기.
    # key가 없어도 오류대신 None을 반환하기 때문에 서버가 멈추지 않는다. (.get())
    message = request.GET.get('name') 
    context = {
        'message' : message,
    }
    return render(request, 'catch.html', context)