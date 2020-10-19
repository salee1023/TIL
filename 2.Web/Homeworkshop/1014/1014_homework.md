# 1014_homework

### 1. 아래의 설명을 읽고 T/F 여부를 작성하시오.

- JavaScript는 single threaded 언어로 한번에 한가지 일 밖에 처리하지 못한다.

  (T)

- setTimeout은 브라우저의 Web API를 사용하는 함수로, Web API에서 동작이 완료되면 Call Stack에 바로 할당된다.  

  (F) **Task Queue**에 있다가 **Call Stack**이 비어있으면 **Event Loop**가 **Call Stack**으로 옮겨준다. 

- Promise 객체를 생성할 때 인자로 받는 callback 함수인 resolve와 reject는 비동기 처리가 성공/실패 했을 경우 어떠한 값을 전달할 지 결정한다. 

  (T)

- Promise 객체의 .then 메서드는 오류 없이 resolve 되었을 때 실행되는 함수이며, .catch 메서드는 도중에 오류가 발생하여 reject 되었을 때 실행되는 함수이다. 

  (T)


---

### 2. JavaScript에서 동기와 비동기 함수의 차이점을 서술하시오.

- **동기 (Synchronous)** : 하나의 코드가 끝나면 다음 코드가 실행된다. (위에서 아래로 순차적)
- **비동기 (Asynchronous)** : `setTimeout()` 함수와 같이 비동기적 함수는 아래 함수가 기다려주지 않고 `setTimeout()`의 응답이 오기전까지 아래 함수가 먼저 실행된다. 



---

### 3. 다음은 axios를 사용하여 API 서버로 요청을 보내고, 응답 데이터를 출력하는 코드이다. (a), (b), (c)에 들어갈 코드를 작성하시오.

```html
axios.___(a)___('https://api.example.com/data')
   .__(b)__(function (response) {
	  console.log(___(c)___)
})
```

(a) : get

(b) : then

(c) : response

