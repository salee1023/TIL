# 0811_homework

### 1.  Semantic Tag

HTML5에서 새롭게 추가된 시맨틱 태그 : `header`   `section`  `footer` 

---



### 2. Input Tag

```html
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>input Tag</title>
</head>
<body>
    <section>
        <form action="#" method="GET">
            <div>
                <label for="name">USERNAME : </label>
                <input type="text" id="name" placeholder="아이디를 입력 해 주세요.">
            </div>
            
            <div>
                <label for="password">PWD : </label>
                <input type="password" id="password" autofocus>
                <input type="submit" value="로그인">
            </div>
        </form>
    </section>
    
</body>
</html>
```

`value` : 입력하려 할 때, 안내문을 지워야하는 번거로움

`placeholder` : 안내문을 보고 싶을 때, 입력값을 지워야하는 번거로움

`<p>` 에 안내문을 새로 써주는 것이 Trend!

---



### 3. 크기 단위

크기 단위 em은 요소에 지정된 상속된 사이즈나 기본 사이즈에 대해 상대적인 사이즈를 설정한다. 즉, 상속의 영향으로 사이즈가 의도치 않게 변경될 수 있는데, 이를 예방하기 위해 HTML 최상위 요소의 사이즈를 기준으로 삼는 크기 단위는 무엇인가?

rem

---



### 4. 선택자

```css
/*  자손 선택자 */
div p {
    color: crimson;
}

/* 자식 선택자 */
div > p {
	color: crimson;
}
```

자손 선택자 : 특정 요소의 자손을 모두 선택한다. (자식, 손자, 후손 모두 포함한다.)

자식 선택자: 특정 요소의 직계 자식만 선택한다. (자식 외에 손자, 후손은 포함하지 않는다.)

















































