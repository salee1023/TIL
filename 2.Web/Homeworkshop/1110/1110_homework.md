# 1110_homework

### 1. 아래의 설명을 읽고 T/F 여부를 작성하시오.

- 동일한 요소에 `v-for`와 `v-if `두 디렉티브가 함께 작성된 경우, 매 반복 시에 `v-if`의 조건문으로 요소의 렌더링 여부를 결정한다.  

  T 

- `v-bind` 디렉티브는 "@", `v-on` 디렉티브는 ":" shortcut(약어)를 제공한다.

  F 반대다.

- `v-model` 디렉티브는 input, textarea, select 같은 HTML 요소와 단방향 데이터 바인딩을 이루기 때문에 `v-model` 속성값의 제어를 통해 값을 바꿀 수 있다.

  F 양방향이다.

---

### 2. computed와 watch의 개념과 그 차이에 대해서 간단히 서술하시오.

`computed` : 

- 특정한 데이터를 가공해서, 새로운 값으로 만들어서 저장하고 싶은 경우에 사용한다.

- 계산된 값은  return하고, key이름은 변수 이름처럼 사용한다. 
- 계산해야 하는 목표 데이터를 정의하는 선언형 프로그래밍 방식이다. 

`watch` :

- 데이터 변경을 관찰하고 반응한다. 
- 단순히 데이터값 저장 뿐만 아니라, 부가적인 기능(로직) 수행도 포함한다. 

- 어떤 조건이 되면, ~~로직을 실행하라는 명령형 프로그래밍 방식이다. 

---

### 3. 다음은 짝수 데이터만 렌더링하는 vue Application의 예시이다. 빈칸 (a), (b), (c) 에 들어갈 코드를 작성하시오.

```html
<div id="app">
    <div __(a)__="num in nums" __(b)__="num % 2 === 0">{{ __(C)__ }}</div>
</div>
    
<script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
    <script>
    const app = new Vue ({
        el: "#app",
        data: {
        nums: [1, 2, 3, 4, 5, 6],
        },
    })
</script>
```

(a) : v-for

(b) : v-if

(c) : num





