# 0813_homework

### 1. CSS flex-direction

Flex box의 주축을 변경하는 flex-direction 의 4가지 값과 각각의 특징을 작성하시오.

`row` : 기본값이다. 가로 방향으로 요소가 쌓인다. (왼->오)

`row-reverse` : 가로 방향으로 요소가 쌓인다. (오->왼)

`column` : 세로 방향으로 요소가 쌓인다. (위 ->아래)

`column-reverse` : 세로 방향으로 요소가 쌓인다. (아래 ->위) 



---



### 2. Bootstrap flex-direction

 flex-direction 의 4가지 요소와 대응하는  bootstrap 클래스를 작성하시오.

`row` : flex-row

`row-reverse` : flex-row-reverse

`column` : flex-column

`column-reverse` : flex-column-reverse



---



### 3. align-items

align-items  속성의 4가지 값과 각각의 특징을 작성하시오. (`flex-direction: row`일 때)

`stretch` : 기본값이다. 컨테이너를 가득 채운다.

`flex-start` : 위

`flex-end` : 아래

`center` : 가운데

`baseline` : 내부 text에 기준선을 맞춘다.



---



### 4. flex-flow

flex-flow 속성은 두가지 속성의 축약형이다. 올바르게 짝지어진 것은?

(1) flex-direction, flex-wrap



---



### 5. Bootstrap Grid System

하단 코드에 Bootstrap Grid System을 적용시키고자 할 때, (a), (b) 각각에 입력해야 할 클래스 이름을 작성하시오.

```html
<div class="__(a)__">
    <div class="__(b)__">
        <div class="col-__(c)__-__(d)__">hello</div>
    </div>
</div>
```

(a) container

(b) row



---



### 6. Breakpoint prefix

Bootstrap Grid System에서 요소의 크기를 지정하기 위해서는 상단의 코드와 같은 형태로 클래스 이름을 지정해야 한다. (c) 와 (d)에 들어갈 값과 그 값들이 가지는 의미를 작성하시오.

(c) `None`  `sm`  `md`  `lg`  `xl`  :  특정 px 조건에 대한 지점을 정한  breakpoints이다. breakpoints를 이용하여 다양한 디바이스에 적합한 페이지를 만들 수 있다. 

(d) number (0~12) : 12개 중에서 사용하려는 수를 나타낸다. 백분율로 설정되기 때문에 부모 요소를 기준으로 크기가 조정된다.







































