# 0922_homework

### 1. SQL 용어 및 개념

1) `스키마` : 관계형 데이터베이스에서 구조와 제약조건에 관련한 전반적인 명세를 기술한 것

2) `테이블` : 열과 행의 모델을 사용해 조직된 데이터 요소들의 집합

3) `컬럼` : 고유한 데이터 형식이 지정되는 열

4) `레코드` : 단일 구조 데이터 항목을 가리키는 행

5) `기본키` : 각 행의 고유값  

---

### 2. SQL 문법

> DML (Data Manipulation Language)

(1) CREATE : 테이블 생성 (DDL)

(2) UPDATE : 데이터 수정

(3) DELETE : 데이터 삭제

(4) SELECT : 데이터 조회

---

### 3. RDBMS, NOSQL

**RDBMS** : 테이블이 서로 연결되어있어 데이터 중복을 방지하고, 데이터를 효율적으로 관리할 수 있다. 스키마가 정해져있어서 명확한 데이터 구조를 알 수 있다. 단, 시스템이 복잡해지면 Query 작성에 어려움이 생기고, 성능이 저하된다.

**NOSQL** : 테이블끼리 연결되어있지 않다. 스키마가 없어서 자유롭게 데이터를 추가하고 관리할 수 있다.  데이터가 자주 변경되지 않고 단순한 경우 효과적이다. 하지만,  데이터 중복이 생겨서 데이터 수정시 중복된 데이터를 모두 관리해줘야하는 단점이 있다.

---

### 4. INSERT INTO

```sql
CREATE TABLE classmates (
	name TEXT,
    age INT,
    address TEXT
);
```

(3) insert into classmates values (address='seoul', age=20, name='salee');

👉 values에는 넣어줄 값만 순서에 맞춰 작성해야한다. *(Error: no such column: address)*

---

### 5. 와일드카드 문자

`%` : 자릿수와 상관없이 문자가 들어온다.

`_` : `_` 의 수 만큼 문자가 들어와야한다.