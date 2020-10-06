# 1006_homework

### 1. 아래의 설명을 읽고 T/F 여부를 작성하시오.

- JSON 포맷의 데이터로 응답하기 위해서는 반드시 DRF를 사용해야 한다.  (F) ex) JsonResponse
- DRF 내장 Form을 통해서만 HTTP Method를 테스트 해볼 수 있다. (F) ex) Postman
- api_view 데코레이터를 사용하지 않아도 HTTP Method에 대한 요청에 응답할 수 있다. (F) DRF에서는 무조건 있어야 한다. 	
- Serializer는 ORM Query 객체를 JSON 포맷으로 직렬화, 또는 그 반대의 작업을 할 때 사용한다. (T)

---

### 2. 다음의 HTTP Method들의 의미를 간략하게 작성하시오.

- GET :  특정 리소스의 표시를 요청한다. 데이터를 받기만 한다.
- POST : 특정 리소스에 데이터를 제출한다. 서버의 상태의 변화를 일으킨다. 
- PUT : 리소스의 현재 표시를 요청한다.
- DELETE : 특정 리소스를 삭제한다.

---

### 3. 아래에서 (a), (b), (c) 에 들어갈 코드를 작성하시오.

```python
@api_view(____(a)____)
def article_create(request):
    serializer = ArticleSerializer(____(b)____)
    if serializer.is_valid(_____(c)_____):
        serializer.save()
    return Response(serializer.data)
```

(a) : ['POST']

(b) : data=request.data

(c) : raise_exception=True