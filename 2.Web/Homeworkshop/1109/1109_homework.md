# 1109_homework

### 1. 아래의 설명을 읽고 T/F 여부를 작성하시오.

- SPA는 Single Pattern Application의 약자이다.

  (F) Single Page Application

- SPA는 웹 애플리케이션에 필요한 모든 정적 리소스를 한 번에 받고, 이후부터는 페이지 갱신에 필요한 데이터만 전달받는다.

  (T)

- Vue.js에서 말하는 '반응형'은 데이터가 변경되면 이에 반응하여, 연결된 DOM이 업데이트되는 것을 의미한다.

  (T)

  


---

### 2. MVVM은 무엇의 약자이고, 해당 패턴에서 각 파트의 역할은 무엇인지 간단히 서술하시오.

M (Model) :  어플리케이션에서 사용되는 데이터이다.

V (View) : 사용자에게 보여지는 부분이다.

VM (ViewModel) : View와 Model을 연결시켜주는 부분이다.



---

### 3. 다음의 빈칸 (a), (b), (c)에 들어갈 코드를 작성하시오.

```html
<div id="app">
    {{ ____(a)____ }}
</div>

<script>
    const app = ____(b)____ ({
        el: ____(c)____,
        data: {
            message: 'Hello World',
        },
    })
</script>
```

(a) : message

(b) : new Vue

(c) : "#app"