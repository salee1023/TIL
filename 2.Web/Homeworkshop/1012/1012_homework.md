# 1012_homework

### 1. 아래의 설명을 읽고 T/F 여부를 작성하시오.

- document.createElement 메서드를 통해 HTML 요소를 생성할 수 있다. (T)
- EventTarget.addEventListener(type, listener)에서 listener 함수는 한개의 매개변수를 허용한다. 이 매개변수는 발생한 이벤트를 설명하는 Event에 기반한 객체이다. (T)
- event.preventDefault 메서드를 통해 이벤트 동작을 취소할 수 있다. (T)	
- 부모 노드에서 자식 노드를 추가하는 유일한 방법은 append 메서드 뿐이다. (F)

---

### 2. DOM Event 에는 다양한 종류의 Event가 존재한다. 아래 제시된 Event들이 각각 어떤 시점에 발생하는지 다음 MDN 문서를 참고하여 간단하게 작성하시오.

- click : 포인팅 장치 버튼이 눌렸다가 놓였을 때
- mouseover : 포인팅 장치가 listener에 등록된 element나 그 자식 element 위로 이동했을 때
- mouseout : 포인팅 장치가 listener에 등록된 element또는 그 자식 element 밖으로 이동했을 때.
- keypress : Shift, Fn, CapsLock 을 제외한 키가 눌린 상태일 때. (연속적으로 실행된다)
- keydown : 키가 눌렸을 때.
- keyup : 키 누름이 해제될 때.
- load : 진행이 성공했을 때.
- scroll : 다큐먼트 뷰나 element가 스크롤되었을 때.
- change : The `change` event is fired for [``](https://developer.mozilla.org/ko/docs/Web/HTML/Element/input), [``](https://developer.mozilla.org/ko/docs/Web/HTML/Element/select), and [``](https://developer.mozilla.org/ko/docs/Web/HTML/Element/textarea) elements when a change to the element's value is committed by the user.

---

### 3. 다음은 버튼을 클릭했을 때, 콘솔창을 통해 메시지를 확인하는 코드이다. (a), (b), (c)

```python
const button = document.___(a)___('button')

button.___(b)____(___(c)___, function () {
  console.log('Button clicked!')  
})
```

(a) : querySelector

(b) : addEventListener

(c) : 'click'