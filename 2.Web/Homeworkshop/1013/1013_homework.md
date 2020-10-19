# 1013_homework

### 1. 아래의 설명을 읽고 T/F 여부를 작성하시오.

- let & const 키워드로 선언한 변수와 var 키워드로 선언한 변수의 유일한 차이점은 변수의 유효범위이다. 

  (F) `var`로 선언된 변수는 선언 이전에 참조할 수 있다. 이 현상을 `hoisting(호이스팅)`이라고 한다.

- "값이 없음"을 표현하는 값으로 null과 undefined  두 종류가 있으며, 둘 다 typeof 연산자에서 undefined가 반환된다. 

  (F) null은 `object`, undefined는 `undefined` 가 반환된다.

- for in 문을 통해 배열의 각 요소를 순회할 수 있다. 

  (F) key와 index를 순회한다.

- == 연산자는 두 변수의 값과 타입이 같은지 비교하고 같다면 true 아니면 false를 반환한다. 

  (F) === 연산자가 값과 타입을 모두 비교한다.

- JavaScript에서 함수는 변수에 할당, 인자로 전달할 수 있으나 함수의 결괏값으로 반환활 수는 없다.

  (F) 함수의 결괏값으로 반환할 수 있다.

---

### 2. 다음의 Array Helper Method 동작을 간략히 서술하시오.

- map - 배열 안의 모든 요소들에 callback함수를 실행하여, **callback 반환값을 요소**로 하는 새로운 배열을 반환한다. (배열을 다른 형식으로 바꿀 때 유용하다!!)

- filter - 배열 안의 모든 요소들중에서 **callback 함수를 통과**하는 모든 요소를 모아 새로운 배열을 반환한다. (filtering)

- find - 주어진 함수를 만족하는 **첫번째 요소**를 반환한다.

- every - 배열 안의 요소중 하나라도 함수를 통과하면 `true` , 아니면 `false` 를 반환한다.

- some - 배열 안의 모든 요소가 함수를 통과하면 `true` , 아니면 `false` 를 반환한다.

- reduce - 배열의 각 요소에 reduce 함수를 실행하고 하나의 결과값을 반환한다. 배열 안의 숫자들의 총합, 평균을 계산할 때 쓰인다.

  ```javascript
  const numbers = [5, 5, 10, 7]
  
  const result = numbers.reduce(function (total, number) {
    console.log(total, number)
    return total + number
  }, 0)
  
  // 0 5
  // 5 5
  // 10 10
  // 20 7
  ```

  

---

### 3. 아래의 숫자 배열에 map 함수를 사용하여, 모든 아이템에 3제곱을 한 새로운 배열을 만드는 코드를 작성하시오.

```javascript
const nums = [1,2,3,4]

const triple = nums.map(num => num**3)

triple //[1, 8, 27, 64]
```



