from django.urls import path
from . import views

app_name = 'articles'
urlpatterns = [
    path('', views.index, name='index'), # 'articles/'
    path('<int:pk>/', views.detail, name='detail'), # 'articles/1'
    path('new/' , views.new, name='new'), # 'articles/new/'
    path('create/', views.create, name='create'),
    path('<int:pk>/delete/', views.delete, name='delete'),
    path('<int:pk>/edit/', views.edit, name='edit'),
    path('<int:pk>/update', views.update, name='update'),
]