# 1112_homework

### 1. 아래의 설명을 읽고 T/F 여부를 작성하시오.

- Vue는 컴포넌트 간 양방향 데이터 흐름을 지향하기 때문에 부모, 자식 컴포넌트 간의 데이터 전달 및 수정이 자유롭다.

  F (단방향이다.)

- v-on 디렉티브는 해당 요소 또는 컴포넌트에서 특정 이벤트 발생 시 전달받은 함수를 실행한다.

  T

- 컴포넌트에서 클릭 이벤트 발생 시 특정 함수를 실행하고자 할 때, @click 혹은 v-on:click 디렉티브를 사용한다.

  F (컴포넌트에서는 @click.native="" 와 같이 처리해준다. // @click은 html태그에서 처리할 때)

- 부모 컴포넌트는 props를 통해 자식 컴포넌트에게 이벤트를 보내고 자식 컴포넌트는 emit을 통해 부모 컴포넌트에게 데이터를 전달한다.

  F (props는 부모가 자식에게 데이터 전달, emit은 자식이 부모에게 이벤트 전달)


---

### 2. Vue는 단방향 데이터 흐름을 지향하는 프론트엔드 프레임워크다. 공식문서를 참고하여 그 이유를 서술하시오.

```
부모 컴포넌트와 자식 컴포넌트가 의사소통하는 것도 중요하지만, 부모와 자식이 명확하게 분리된 상태로 유지되는 것도 중요하다. 
단방향으로 데이터를 보내면, 각 컴포넌트의 코드를 유지 및 관리하기가 쉽고 재사용도 쉽게 할 수 있다.
```

---

### 3. 다음은 자식 컴포넌트에서 이벤트를 발생시켜 부모 컴포넌트의 함수를 실행하는 코드이다. 빈칸 (a), (b), (c)에 들어갈 코드를 작성하시오.

- Input 컴포넌트의 버튼을 누르면 addTodo 이벤트가 발생한다. (이벤트 발생 시 data의 text 값도 함께 전달한다.)
- TodoList 컴포넌트에서 addTodo 이벤트가 발생하면, onAddTodo 함수를 실행한다.
- onAddTodo 함수에서는 자식 컴포넌트에서 전달받은 값을 console.log 함수를 통해 출력한다.

```html
<template>
  <div>
      <input v-model="text" type="text">
      <button @click="onClick">추가</button>
  </div>
</template>

<script>
export default {
    name: 'Input',
    data: function () {
        return {
            text: '',
        }
    },
    methods: {
        onclick: function () {
            __(a)__('addTodo', this.text)
        }
    }
}
</script>

<style>

</style>
```

```vue
<template>
  <input __(b)__>
</template>

<script>
import Input from './Input'

export default {
    name: 'TodoList',
    components:{
        Input: Input,
    },
    methods: {
        __(c)__
    }
}
</script>

<style>

</style>
```

(a) : this.$emit

(b) : @addTodo="onAddTodo "

(c) : onAddTodo : function (text) {

​			console.log(text)

​		}

