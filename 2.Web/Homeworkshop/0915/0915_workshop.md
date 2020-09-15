# 0915_workshop



- 프로젝트 폴더 (crud)  에 `media` 폴더를 만든다.

```
crud/
	media/
```



- `settings.py`에 media를 참조할 때 사용할 **주소**와 업로드한 **파일을 모아둘 경로**를 지정한다.

```python
# settings.py

# 사용자가 업로드 한 파일을 참조할 때 생성되는 주소 (실제 위치한 디렉토리 아님)
MEDIA_URL = '/media/'

# 사용자가 업로드 한 파일이 위치하는 공간
MEDIA_ROOT = BASE_DIR / 'media'
```



- media파일에 접근할 수 있도록 프로젝트의 `urls.py`에 경로를 넣어준다.

```python
# urls.py

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('articles/', include('articles.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

👉 이렇게 하면 `Django` 가 MEDIA_URL(미디어 파일 접근 url)와 MEDIA_ROOT(실제 미디어 파일 위치)를 연결시켜 media 파일에 접근할 수 있도록 해준다.



- models.py에 media를 저장할 방식을 정해준다. 

```python
# models.py
from django.db import models

# Create your models here.
class Article(models.Model): 
    title = models.CharField(max_length=10)
    content = models.TextField()
    image = models.ImageField(blank=True, upload_to='%Y/%m/%d/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
```

👉 `upload_to='%Y/%m/%d/'` : FileField의 upload_to 속성을 상속받아서 저장 경로와 저장이름을 지정한다.

