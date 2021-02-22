from django.urls import path
from . import views


app_name = 'reservations'
urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('<int:pk>/', views.detail, name='detail'),
    path('<int:pk>/comments_create/', views.comments_create, name='comments_create'),
]