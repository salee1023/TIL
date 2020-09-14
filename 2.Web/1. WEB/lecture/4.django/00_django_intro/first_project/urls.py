"""first_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path, include


# http://127.0.0.1:8000/articles/블라블라
# -> articles 앱에서 관리
# http://127.0.0.1:8000/pages/블라블라
# -> pages 앱에서 관리
urlpatterns = [
    path('admin/', admin.site.urls),
    # 'articles/'로 시작하는 URL 요청은 articles 앱의 urls.py에서 처리해라! 위임.
    path('articles/', include('articles.urls')),
    path('pages/', include('pages.urls')),
]
