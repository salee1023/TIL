"""first_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
# articles에 있는 기능을 불러와야 사용할 수 있다!
from articles import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # 사용자가 index/ 라는 주소로 요청을 하면, _______기능을 실행해라!
    path('index/', views.index),
    path('dinner/', views.dinner),
    path('hello/<str:name>/', views.hello),
    path('dtl-practice/', views.dtl_practice),
    path('throw/', views.throw),
    path('catch/', views.catch),
]
