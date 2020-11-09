# Vue 기초 + Directive 복습 흐름

MVC, MTV, M, V VM

1. DOM(View)이랑 Data(Model)를 연결시킨 반응형 웹 애플리케이션을 만들고 싶다.
2. Vue 인스턴스 (ViewModel)를 생성한다. 
   - `el` : Vue 인스턴스와 DOM을 마운트(연결) 시켜주는 옵션
   - `data` :  Vue 인스턴스가 갖고 있는 데이터 객체
   - `methods` : Vue 인스턴스의 메서드 (Arrow Function금지! this가 window 전역 객체가 바인딩 됨.)
3. DOM에 연결된 데이터들을 다양ㅎ나 방법으로 조작하고 싶다. -> 디렉티브(`v-` 로 시작하는 특수한 속성)
   - `v-for`  : 반복문
   - `v-if `  `v-else-if`  `v-else`  : 조건문
   - `v-show`  :  `v-if` 는 false면 랜더링조차 안하지만, `v-show`는 랜더링을 하고 false면 `display: none`으로 안보이게 해준다.
   -  `v-text`  `v-html`  :  `v-text` 는 text자체로 인식, `v-html`은 태그로 인식한다.
   - `v-bind` : HTML 표준 속성을 연결한다. 
   - `v-model` : 양방향 바인딩
   - `v-on` : 이벤트 핸들링

