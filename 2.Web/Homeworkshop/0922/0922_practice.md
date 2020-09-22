

# 0922_practice

### 1. SQL ORM 비교하기

> user 테이블 전체 데이터를 조회하시오.

```sql
SELECT *
FROM users_user;
```

```
1,"정호","유",40,"전라북도",016-7280-2855,370
2,"경희","이",36,"경상남도",011-9854-5133,5900
3,"정자","구",37,"전라남도",011-4177-8170,3100
4,"미경","장",40,"충청남도",011-9079-4419,250000
5,"영환","차",30,"충청북도",011-2921-4284,220
..생략
```

```python
User.objects.all()
```

```
<QuerySet [<User: User object (1)>, <User: User object (2)>, <User: User object (3)>, <User: User object (4)>, <User: User object (5)>, <User: User object (6)>, <User: User object (7)>, <User: User object (8)>, '...(remaining elements truncated)...']>
```

---

>id가 19인 사람의 age를 조회하시오.

```sql
SELECT age
FROM users_user
WHERE id=19;
```

```
age
---
26
```

```python
User.objects.filter(pk=19).values('age')
```

```
<QuerySet [{'age': 26}]>
```

---

> 모든 사람의 age를 조회하시오.

```sql
SELECT age
FROM users_user;
```

```
age
---
40
36
37
40
..생략
```

```python
User.objects.values('age')
```

```
<QuerySet [{'age': 40}, {'age': 36}, {'age': 37}, {'age': 40}, {'age': 30}, {'age': 26}, {'age': 18}, {'age': 33}, {'age': 23}, '...(remaining elements truncated)...']>
```

---

> age가 40 이하인 사람들의 id와 balance를 조회하시오.

```sql
SELECT id, balance
FROM users_user
WHERE age<=40;
```

```
id   balance
---  -------
1    370
2    5900
3    3100
4    250000
5    220
..생략
```

```python
User.objects.filter(age__lte=40).values('id','balance')
```

```
<QuerySet [{'id': 1, 'balance': 370}, {'id': 2, 'balance': 5900}, {'id': 3, 'balance': 3100}, {'id': 4, 'balance': 250000}, {'id': 5, 'balance': 220}, '...(remaining elements truncated)...']>
```

---

> last_name이 '김'이고 balance가 500 이상인 사람들의 first_name을 조회하시오.

```sql
SELECT first_name FROM users_user
WHERE last_name='김' AND balance >= 500;
```

```
first_name
----------
예진
서현
서영
영일
옥자
..생략
```

```python
User.objects.filter(last_name='김',balance__gte=500).values('first_name')
```

```
<QuerySet [{'first_name': '예진'}, {'first_name': '서현'}, {'first_name': '서영'}, {'first_name': '영일'}, {'first_name': '옥자'}, '...(remaining elements truncated)...']>
```

---

> first_name이 '수'로 끝나면서 행정구역이 경기도인 사람들의 balance를 조회하시오.

```sql
SELECT balance
FROM users_user
WHERE first_name LIKE '%수' AND country='경기도';
```

```
balance
-------
590
370
```

```python
User.objects.filter(first_name__endswith='수', country='경기도').values('balance')
```

```
<QuerySet [{'balance': 590}, {'balance': 370}]>
```

---

> balance가 2000 이상이거나 age가 40 이하인 사람의 총 인원수를 구하시오.

```sql
SELECT COUNT(*) 
FROM users_user
WHERE balance >= 2000 OR age <= 40;
```

```
COUNT(*)
--------
100
```

```python
User.objects.filter(Q(balance__gte=2000) | Q(age__lte=40)).count()
```

```
100
```

---

> phone 앞자리가 '010'으로 시작하는 사람의 총원을 구하시오.

```sql
SELECT COUNT(*)
FROM users_user
WHERE phone LIKE '010%';
```

```
COUNT(*)
--------
21
```

```python
User.objects.filter(phone__startswith='010').count()
```

```
21
```

---

>이름이 '김옥자'인 사람의 행정구역을 경기도로 수정하시오.

```sql
UPDATE users_user 
SET country='경기도'
WHERE first_name='옥자' AND last_name='김';

SELECT country
FROM users_user
WHERE first_name='옥자' AND last_name='김';
```

```
country
-------
경기도
```

```python
user = User.objects.get(first_name='옥자',last_name='김') 
user.country='경기도'
user.save()
```

```
<QuerySet [{'country': '경기도'}]>
```

---

> 이름이 '백진호'인 사람을 삭제하시오.

```sql
DELETE FROM users_user
WHERE first_name='진호' AND last_name='백';

SELECT *
FROM users_user
WHERE first_name='진호' AND last_name='백'; 
```

```python
user = User.objects.get(first_name='진호', last_name='백')
user.delete()
```

```
(1, {'users.User': 1})
```

---

> balance를 기준으로 상위 4명의 first_name, last_name, balance를 조회하시오.

```sql
SELECT first_name, last_name, balance
FROM users_user
ORDER BY balance DESC LIMIT 4;
```

```
first_name  last_name  balance
----------  ---------  -------
순옥          김          1000000
은주          김          950000
미경          이          890000
동현          이          790000
```

```python
User.objects.order_by('-balance').values('first_name','last_name','balance')[:4]
```

```
<QuerySet [{'first_name': '순옥', 'last_name': '김', 'balance': 1000000}, {'first_name': '은주', 'last_name': '김', 'balance': 950000}, {'first_name': '미경', 'last_name': '이', 'balance': 890000}, {'first_name': '동현', 'last_name': '이', 'balance': 790000}]>
```

---

> phone에 '123'을 포함하고 age가 30 미만인 정보를 조회하시오.

```sql
SELECT *
FROM users_user
WHERE phone LIKE '%123%' AND age < 30;
```

```
id  first_name  last_name  age  country  phone         balance
--  ----------  ---------  ---  -------  ------------  -------
93  하은          손        18   전라남도  02-9618-1232   4800
```

```python
User.objects.filter(phone__contains='123', age__lt=30).values()
```

```
<QuerySet [{'id': 93, 'first_name': '하은', 'last_name': '손', 'age': 18, 'country': '전라남도', 'phone': '02-9618-1232', 'balance': 4800}]>
```

---

> phone이 '010'으로 시작하는 사람들의 행정 구역을 중복 없이 조회하시오.

```sql
SELECT DISTINCT country 
FROM users_user
WHERE phone LIKE '010%';
```

```
country
-------
충청북도
경상북도
경기도
제주특별자치도
경상남도
전라남도
강원도
전라북도
```

```python
User.objects.filter(phone__startswith='010').values('country').distinct()  
```

```
<QuerySet [{'country': '충청북도'}, {'country': '경상북도'}, {'country': '경
기도'}, {'country': '제주특별자치도'}, {'country': '경상남도'}, {'country': '전라남도
'}, {'country': '강원도'}, {'country': '전라북도'}]>
```

---

> 모든 인원의 평균 age를 구하시오.

```sql
SELECT AVG(age)
FROM users_user;
```

```
AVG(age)
----------------
28.3434343434343
```

```python
User.objects.aggregate(age_value=Avg('age')).get('age_value')
```

```
28.343434343434343
```

---

> 박씨의 평균 balance를 구하시오.

```sql
SELECT AVG(balance)
FROM users_user
WHERE last_name='박';
```

```
AVG(balance)
----------------
196114.285714286
```

```python
User.objects.filter(last_name='박').aggregate(balance_value=Avg('balance')).get('balance_ value')
```

```
196114.2857142857
```

---

> 경상북도에 사는 사람 중 가장 많은 balance의 액수를 구하시오.

```sql
SELECT MAX(balance)
FROM users_user
WHERE country='경상북도';
```

```
MAX(balance)
------------
400000
```

```python
User.objects.filter(country='경상북도').aggregate(balance_value=Max('balance')).get('bala nce_value')
```

```
400000
```

---

> 제주특별자치도에 있는 사람 중 balance가 가장 많은 사람의 first_name을 구하시오.

```sql
SELECT first_name
FROM users_user
WHERE country='제주특별자치도'
ORDER BY balance DESC LIMIT 1;
```

```
first_name
----------
순옥
```

```python
User.objects.filter(country='제주특별자치도').order_by('-balance').values('first_name')[:1]
```

```
<QuerySet [{'first_name': '순옥'}]>
```

