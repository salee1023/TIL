# 0811_workshop

### 1. Semantic Tag

제시된  semantic.html과  semantic.css을 수정하여 다음 이미지와 같은 형태가 되도록 코드를 작성하시오.

```html
<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link rel="stylesheet" href="semantic.css">
  <title>Layout Practice</title>
</head>
<body>
  <header class="background1 size border">
    <h1 class="align">header</h1>
  </header>
  <nav class="background1 size border">
    <h2>nav</h2>
  </nav>
  <section class="background1 size  display s_size border">
    <h2>section</h2>
    <article class="background2 size border">
      <h3>article1</h3>
      <h3>article2</h3>
    </article>
  </section>
  <aside class="background1 size display a_size a_verticle border">
    <h2>aside</h2>
  </aside>
  <footer class="background1 size border">
    <h2>footer</h2>
  </footer>
</body>
</html>
```

```css
body {
  font-family: Arial;
  width: 800px;
}

/* 모든 스타일링 요소를 클래스로 만들어 사용합니다. */
/* 1. airticle 태그는 white로 나머지 시멘틱 태그는 lightgrey로 배경색을 바꿔주세요. */
.background1 {
  background-color: lightgray;
}
.background2 {
  background-color: white;
}

/* 2. 모든 시멘틱 태그의 margin과 padding을 4px로 만들어주세요. */
.size {
  margin: 4px;
  padding: 4px;
}

/* 3. h1 태그를 중앙 정렬 시켜주세요. */
.align {
  text-align: center;
}

/* 4. section과 aside 태그의 display를 inline-block으로 바꿔주세요. */
.display {
  display: inline-block;
}
/* 5. section 태그는 width 482px height 300px, aside 태그는 width 280px height 300px로 만들어주세요.*/
.s_size {
  width: 482px;
  height: 300px;
}
.a_size {
  width: 280px;
  height: 300px;
}
/* 6. aside 태그에 vertical-align속성의 값을 top으로 적용해주세요.*/
.a_verticle {
  vertical-align: top;
}
/* 7. 모든 semantic 태그의 border 둘레를 4px로 만들어주세요. */
.border {
  border-radius: 4px;
}
```




