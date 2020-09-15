# 0915_homework

#### 1. static 파일 기본 설정

```python
# settings.py
STATICFILES_DIRS = [
    BASE_DIR / 'assets',
]
```



---



#### 2. media 파일 기본 설정

```python
# settings.py
# 사용자가 업로드 한 파일을 참조할 때 생성되는 주소 (실제 위치한 디렉토리 아님)
MEDIA_URL = '/media/'

# 사용자가 업로드 한 파일이 위치하는 공간
MEDIA_ROOT = BASE_DIR / 'uploaded_files'
```



---



#### 3. Serving Files

```python
from django.conf import __(a)__
from __(b)__ import __(c)__

urlpatterns = [
    ...
] + static(__(d)__)
```

(a) : settings

(b) : django.conf.urls.static

(c) : static

(d) : settings.MEDIA_URL, document_root=settings.MEDIA_ROOT









