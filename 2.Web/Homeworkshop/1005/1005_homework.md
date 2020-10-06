# 1005_homework

### 1. 아래의 설명을 읽고 T/F 여부를 작성하시오.

- URI는 정보의 자원을 표현하고, 자원에 대한 행위는 HTTP Method로 표현한다. (T)

- HTTP Method는 GET과 POST 두 종류가 있다.  (F) `GET` `POST` `PUT` `DELETE`

- 일반적으로 URI 마지막에 슬래시(/) 는 포함하지 않는다. (T) 장고만 붙임	

- https://www.fifa.com/worldcup/teams/team/43822/create/는 계층 관계를 잘 표현한 RESTful한 URI라고 할 수 있다.  (F) `create`와 같이 행위가 들어가있고, `teams/team/43822/` 와 같이 의미가 불분명하기 때문에 RESTful하지 않다.

---

### 2. 다음의 HTTP status code의 의미를 간략하게 작성하시오.

- 200 : OK 요청이 성공적으로 전송됨 (성공)
- 400 : Bad Request 잘못된 문법으로 인해 서버가 요청을 이해할 수 없음 (클라이언트 에러)
- 401: Unauthorized 비인증된 요청이 들어왔다 (클라이언트 에러)
- 403 : Forbidden 클라이언트가 콘텐츠에 접근할 권리가 없다 (클라이언트 에러)
- 404 : Not Found 서버가 요청받은 리소스를 찾을 수 없다 (클라이언트 에러)
- 500 : Internal Server Error 서버가 처리방법을 모르는 상황이 발생했다 (서버 에러)

---

### 3. 아래의 모델을 바탕으로 Serializer를 정의하려 한다. serializers.py 파일에 StudentSerializer를 작성하시오.

```python
class Student(models.Model):
    name = models.TextField()
    age = models.CharField(max_length=20)
    address = models.TextField()
```

```python
from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Student
        fields = '__all__'
```

---

### 4. Serializer를 DRF(Django REST Framework) 공식 문서를 참고하여 간단하게 설명하시오.

👉 Serializer는 복잡한 데이터를 JSON, MXL같은 다른 content type으로 쉽게 랜더링하게 도와준다.

