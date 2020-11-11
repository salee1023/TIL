# 1111_practice

### 1. 아래의 설명을 읽고 T/F 여부를 작성하시오.

- Vue의 `Life Cycle Hook`에서 `created` Hook은 Vue template에 작성한 요소들이 DOM에 다 그려지는 시점에 실행된다. 

  F (인스턴스가 작성된 후 호출된다.)

- `npm`은 Node Package Manager의 약자이며, `npm`을 통해 설치한 package 목록은 `package.json` 파일에 자동으로 작성된다.

  T

- Vue CLI를 통해 만든 프로젝트는 브라우저가 아닌 node.js 환경이기 때문에 DOM조작이나 web API 호출 등 Vanilla JS에서의 기능을 사용할 수 없다.

  F  (vanilla JS기능을 사용할 수 있다. CLI는 분리된 파일을 합쳐주는 역할을 한다. )

---

### 2. Vue Router에서 설정하는 history mode가 무엇을 뜻하는지 서술하시오.

```
vue-router의 기본 설정은 hash 모드이다. 
hash모드에서는 주소창에 'http://localhost:8080/#/'와 같이'#'이 붙는다.
hash모드에서는 URL이 변경될 때 페이지가 다시 로드되지 않는다.
history 모드에는 '#'이 없다.
SPA이기 때문에 처음 경로부터 쭉 사용하면 문제 없지만, 사용자가 직접 중간 url에 접속하면 404오류가 발생한다. (hash모드에서는 오류 발생 X)
이 문제를 해결하기 위해서는 어떤 경로로 접근한던간에 index.html 페이지를 제공하면 된다.
```

---

### 3. Vue Life Cycle Hook을 참고하여, 다음 Vue application을 실행했을 때 console 창에 출력되는 메시지를 작성하시오.

```html
<script>
export default {
	name: 'HelloWorld',
    created: function () {
        console.log('created!')
    },
    mounted: function () {
        console.log('mounted!')
    },
    updated: function () {
         console.log('updated!')
    },
};
</script>
```

```
created!
mounted!
```



