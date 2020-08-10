# 0801_workshop

### 1. img tag

폴더 안의 my_photo.png를 출력하는 <img> tag

```html
<!DOCTYPE html>
<html>
    <head>
        <meta charset="UTF-8">
        <title>img tag</title>
    </head>
    <body>
        <img src="C:\Users\Windows 10\Desktop\TIL\ssafy\image\my_photo.png" alt="ssafy">
    </body>
</html>
```



---



### 2. 파일 경로

​	위와 같이 경로를 **절대경로**로 작성 할 시, github에 업로드 하거나 전체 폴더의 위치가 변경 되었을 대 이미지를 불러 올 수 없게 된다. 이를 해결하려면 이미지 경로를 **상대경로**로 바꾸어 작성하면 된다.

`바뀐주소` : ..\image\my_photo.png

```python
<!DOCTYPE html>
<html>
    <head>
        <title>img tag</title>
    </head>
    <body>
        <img src="..\image\my_photo.png" alt="ssafy" width="300px">
    </body>
</html>
```



---



### 3. Hyper Link

​	출력된 my_photo.png 이미지를 클릭하면 ssafy.com으로 이동하게 한다.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>img tag</title>
    </head>
    <body>
        <a href="https://www.ssafy.com">
            <img src="..\image\my_photo.png" alt="ssafy">
        </a>
    </body>
</html>
```



---



### 4. 선택자

​	아래의 코드를 작성하고 결과를 확인 하시오.

```html
<!-- 1. :nth-child() -->
<!DOCTYPE html>
<html>
    <head>
        <title>img tag</title>
        <style>
            #ssafy > p:nth-child(2) {
                color:red;
            }
        </style>
    </head>
    <body>
        <div id="ssafy">
            <h2>어떻게 선택 될까?</h2>
            <p>첫번째 단락</p>
            <p>두번째 단락</p>
            <p>세번째 단락</p>
            <p>네번째 단락</p>
        </div>
    </body>
</html>
```

**결과** : **첫번째 단락**이 **빨간색**으로 변한다.

```html
<!-- 2. :nth-of-type() -->
<!DOCTYPE html>
<html>
    <head>
        <title>img tag</title>
        <style>
            #ssafy > p:nth-of-type(2) {
                color:blue;
            }
        </style>
    </head>
    <body>
        <div id="ssafy">
            <h2>어떻게 선택 될까?</h2>
            <p>첫번째 단락</p>
            <p>두번째 단락</p>
            <p>세번째 단락</p>
            <p>네번째 단락</p>
        </div>
    </body>
</html>
```

**결과** : **두번째 단락**이 **파란색**으로 변한다. 



`:nth-child()` : 타입과 상관없이 형제 사이에서의 순서에 따라 요소를 선택한다.

`:nth-of-type()` : 타입과 일치하는 형제 사이에서의 순서에 따라 요소를 선택한다.


