# 0728_workshop

### 1. 무엇이 중복일까

> 문자열을 전달 받아 해당 문자열에서 중복해서 나타난 문자들을 담은 list를 반환하는  duplicated_letters 함수를 작성하시오.

```python
def duplicated_letters(words):
    duplicate = []
    for word in words:
        # 문자가 2번 이상 나오고, 중복리스트에 없다면, 리스트에 추가
        if (words.count(word) >= 2) and (word not in duplicate):
            duplicate.append(word)
    return print(duplicate)

duplicated_letters('apple')
duplicated_letters('banana')    
```

```python
# list comprehension 이용
def duplicated_letters(words):
    result = list({word for word in words if(words.count(word) >= 2)})
    return print(result)


duplicated_letters('apple')
duplicated_letters('banana')  
```





### 2. 소대소대

> 문자열을 전달 받아 해당 문자열을 소문자와 대문자가 번갈아 나타나도록 변환하여 반환하는  low_and_up 함수를 작성하시오. 이때, 전달 받는 문자열은 알파벳으로만 구성된다.

```python
def low_and_up(words):
    # 새로운 문자를 넣어줄 곳
    new_word = ''
    # 몇 번째 글자인지 판별
    count = 1
    for word in words:
        # 홀수는 소문자
        if count % 2:
            new_word += word.lower()
            count += 1
        #짝수는 대문자
        else:
            new_word += word.upper()
            count += 1

    return print(new_word)        
            
low_and_up('apple')
low_and_up('banana')    
```

```python
# enumerate() 사용
def low_and_up(words):
    new_word = ''
    for idx, char in enumerate(words):
        if idx % 2:
            new_word += char.upper()
        else:
            new_word += char.lower()    

    return print(new_word)        
            
low_and_up('apple')
low_and_up('banana')    
```







### 3. 숫자의 의미

> 정수 0부터 9까지로 이루어진 list를 전달 받아, 연속적으로 나타나는 숫자는 하나만 남기고 제거한 list를 반환하는 lonely 함수를 작성하시오. 이때, 제거된 후 남은 수들이 담긴 list의 요소들은 기존의 순서를 유지해야 한다.

```python
def lonely(numbers):
    # 새로운 숫자 리스트 선언
    new_numbers = []
    # 처음 숫자는 넣어줌
    new_numbers.append(numbers[0])
    i = 0
    for num in numbers:
        # 새로 만든 리스트속 마지막 숫자와 같으면 넘어감
        if num == new_numbers[i]:
            continue
        # 다르다면 새로 넣어주고 새로운 리스트 인덱스 +1
        else:
            new_numbers.append(num)
            i += 1
    return print(new_numbers)    


lonely([1, 1, 3, 3, 0, 1, 1])
lonely([4, 4, 4, 3, 3])
```

```python
# enumerate() 사용
def lonely(numbers):
    new_numbers = []
    for idx, num in enumerate(numbers):
        if idx == 0:
            new_numbers.append(num)
        elif new_numbers[-1] != num:
            new_numbers.append(num)    
    return print(new_numbers)    


lonely([1, 1, 3, 3, 0, 1, 1])
lonely([4, 4, 4, 3, 3]) 
```

