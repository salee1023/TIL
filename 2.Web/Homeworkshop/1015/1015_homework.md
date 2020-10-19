# 1015_homework

### 1. 아래의 설명을 읽고 T/F 여부를 작성하시오.

- Event Loop는 Call Stack이 비워지면 Task Queue의 함수들을 Call Stack으로 할당하는 역할을 한다.

  (T)

- XMLHTTPRequest(XHR)은 AJAX 요청을 생성하는 JavaScript API이다. XHR의 메서드로 브라우저와 서버간의 네트워크 요청을 전송할 수 있다.  

  (T)

- axios는 XHR(XMLHTTPRequest)을 보내고 응답 결과를 Promise 객체로 반환해주는 라이브러리이다.

  (T)

  


---

### 2. 아래의 코드가 실행되었을 때 Web API, Task Queue, Call Stack 그리고 Event Loop에서 어떤 동작이 일어나는지 서술하시오.

```javascript
console.log('Hello SSAFY!')

setTimeout(function () {
    console.log('I am from setTimeout')
},1000)

console.log('Bye SSAFY!')
```

1. `console.log('Hello SSAFY!')` 이 **Call Stack**에 push 되고  `Hello SSAFY!` 를 출력하고 pop된다.
2. `setTimeout`은 브라우저에서 제공하는 API이므로 **Web API**로 호출된다. **Call Stack**에서는 push되고 호출이 완료 후 **pop**된다.  
3. `console.log('Bye SSAFY!')`  이 **Call Stack**에 push 되고  `Bye SSAFY!` 를 출력하고 pop된다. **Web API**에서는 setTimeout의 타이머가 작동중이다. 
4. **Web API** 작동이 끝나면, callback 함수(`function () { console.log('I am from setTimeout') }`)를  **Task Queue** 에 넣는다.
5. **Event Loop**이 **Call Stack**이 비어있으면 **Task Queue**의 첫번째 요소를 **Call Stack** 에 넣는다.
6. `console.log('I am from setTimeout')` 이 실행되고 pop된다.



---

### 3. 위 2번 문제의 코드에서 비동기 함수 부분을 Promise 객체를 사용하여 아래와 같은 출력 결과가 나오도록 다시 작성하시오.

```html
Hello SSAFY!
I am from setTimeout
Bye SSAFY!
```

```javascript
console.log('Hello SSAFY!')

const promise = new Promise(function (resolve, reject) {
    setTimeout(function () {
        console.log('I am from setTimeout')
        resolve('Bye SSAFY!')
    },1000)
})
promise.then(function (res) {
    console.log(res)
})
```

