# 0819_Homework

### 1. Model 반영하기

> 아래와 같이 Django에서 선언한 Model을 실제 Database에 반영하는 과정을 뜻하는 용어와 이와 관련된 명령어들을 작성하시오.

```python
class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
```

**Migrations**

`makemigration` : migration 파일(설계도)를 만든다.

`migrate` : 설계도를 실제 DB에 반영한다.

`sqlmigrate` : 설계도가 SQL문으로 어떻게 해석될 지 미리 확인할 수 있다.

`showmigrations` : 설계도들의 migrate현황을 알 수 있다.



### 2. Model 변경사항 저장하기

> 위에서 선언한 Model을 Database에 최종 반영하기 전에 Model의 변경 사항을 저장하고자 한다. 이를 위한 명령어를 수행했을 대 생성되는 파일의 내용을 확인하고, 해당 내용에 대응되는 SQL문을 확인하여 작성하시오.

```
CREATE TABLE "articles_article" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "title" varchar(100) NOT NULL, "content" text NOT NULL;
COMMIT;
```





### 3. Python Shell

> Django에서 사용 가능한 모듈 및 메서드를 대화식 Python Shell에서 사용하려고 할 때, 어떠한 명령어를 통해 해당 Shell을 실행할 수 있는지 작성하시오.

```bash
$ python manage.py shell_plus
```







### 4. Django Model Field

> Django 에서 Model을 정의할 때 사용할 수 있는 [필드 타입](https://docs.djangoproject.com/en/3.1/ref/models/fields/#emailfield)을 5가지 이상 작성하시오.

`CharField(max_length=100)` :  길이에 제한을 둔 문자열을 넣을 때 사용한다.

`TextField()` : 글자 수가 많은 경우 사용한다.

`DateTimeField(auto_now_add=True)` : 값을 처음 넣을 때, 날짜와 시간을 넣어준다. (최초 생성 일자)

`DateTimeField(auto_now=True)` : 값을 save할 때의 날짜와 시간으로 덮는다. (최종 수정 일자)

`EmailField(max_length=100)` : 유효한 이메일 주소인지 확인한다.

`ImageField (upload_to=None, height_field=None, width_field=None,max_length=100, **options)'`: 

`FileField(upload_to=None,max_length=100,** options)`







