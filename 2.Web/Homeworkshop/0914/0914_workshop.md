# 0914_workshop



- Bootstrap Download 페이지에서 **Compiled CSS and JS**를 다운로드한다.



- 프로젝트 폴더 (crud)  에 `static` 폴더를 만들고, `CSS `폴더와 `JS` 폴더를 넣는다.

```
crud/
	static/
		css/
		js/
```



- settings.py에 static 폴더의 경로를 입력해준다.

```python
# settings.py

STATICFILES_DIRS = [
    BASE_DIR / 'crud' / 'static',
]
```

👉 이렇게 하면 `Django` 가 static 파일을 `STATICFILES_DIRS`안에 있는 경로에서 불러오게 된다.



- base.html에 static폴더의 `CSS`와 `JS`를 적용시킨다.

```html
# base.html
{% load static %}

<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link rel="stylesheet" href="{% static 'css/bootstrap.css' %}">
  <title>Document</title>
</head>
<body>
  <div class="container">
    {% block content %}
    {% endblock %}
  </div>
  </script>
  <link rel="stylesheet" href="{% static 'js/bootstrap.js' %}">
</body>
</html>
```

👉 base.html 최상단에 `{% load static %}` 을 넣어 {% static %} 태그를 따로 불러와준다.

👉 `<link rel="stylesheet" href="{% static 'css/bootstrap.css' %}">` : link태그로 적용할 static파일의 경로를 설정한다.

👉 ` <link rel="stylesheet" href="{% static 'js/bootstrap.js' %}">` :link태그로 적용할 static파일의 경로를 설정한다.



