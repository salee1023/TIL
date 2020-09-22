# 0818_workshop

### 1. intro/urls.py

```python
from django.urls import path
from . import views

app_name = 'pages'
urlpatterns = [
    path('dinner/<str:menu>/<int:people>/', views.dinner, name='dinner'),
]
```



### 2. pages/views.py

```python
from django.shortcuts import render
def dinner(request, menu, people):
    context = {
        'menu': menu,
        'people' : people
    }
    return render(request, 'pages/dinner.html', context)    
```



### 3. templates/dinner.html

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <h2>저녁 메뉴</h2>
    <h2>저녁 먹을 사람?! {{people}}명</h2>
    <h2>어떤 메뉴?! {{menu}}</h2>
    
</body>
</html>
```

