# 0727_workshop

### 1. 평균 점수 구하기

> key 값으로 과목명, value 값으로 점수를 가지는 dictionary를 전달 받아, 전체 과목의 평균 점수를 반환하는 함수 get_dict_avg 함수를 작성하시오.

```python
def get_dict_avg(scores):   
    return print(sum(scores.values())/ len(scores.values()))

get_dict_avg({
    'python' : 80,
    'algorithm' : 90,
    'django' : 89,
    'web' : 83
})
```





### 2. 혈액형 분류하기

> 여러 사람의 혈액형(A, B, AB, O)에 대한 정보가 담긴 list를 전달 받아, key는 혈액형의 종류, value는 사람 수인 dictionary를 반환하는  count_blood 함수를 작성하시오. 

```python
# 1. in 연산자 활용하기
def count_blood(bloods):
    blood_dict = {}
    for blood in bloods:
        # 두번째 이상 찾은 혈액형일 때
        if blood in blood_dict:
            blood_dict[blood] += 1
        # 처음 찾은 혈액형일 때
        else:
            blood_dict[blood] = 1       

    return print(blood_dict)    


count_blood([
    'A' , 'B', 'A', 'O', 'AB', 'AB',
    'O' , 'A', 'B', 'O', 'B', 'AB',
    ])
```

```python
# .get() 활용하기
def count_blood(bloods):
    blood_dict = {}
    for blood in bloods:
        # 값이 없으면  <0 + 1>
        # 값이 있으면 <1 + 1>
        blood_dict[blood] = blood_dict.get(blood,0)+1
    return print(blood_dict)    


count_blood([
    'A' , 'B', 'A', 'O', 'AB', 'AB',
    'O' , 'A', 'B', 'O', 'B', 'AB',
    ])
```



