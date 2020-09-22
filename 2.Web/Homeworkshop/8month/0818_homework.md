# 0818_homework

### 1. MTV

Django는 MTV 디자인 패턴으로 이루어진 Web Framework이다. 여기서 MTV는 무엇의 약자이며 각각 MVC 디자인 패턴과 어떻게 매칭 되는지 작성하시오.

- MTV

  M (Model) : 데이터를 처리하는 로직을 담당한다.

  T (Templates) : 사용자의 요청에 따른 데이터를 사용자에게 보여준다.

  V (View) : Model과 Templates 사이를 이어주는 로직을 담당한다.



- MTV & MVC

  |    MTV    |    MVC     |
  | :-------: | :--------: |
  |   Model   |   Model    |
  | Templates |    View    |
  |   View    | Controller |





### 2. URL

`Variable Routing` 은 Django 에서 URL 자체를 변수처럼 사용해서 동적으로 주소를 만드는 것을 의미한다. 



### 3. Template

Django 프로젝트는 render할 template 파일들을 찾을 때, 기본적으로 settings.py에 등록된 각 앱 폴더 안의 `templates` 폴더 내부를 탐색한다. 



### 4. Static web and Dynamic web

Static web page와 Dynamic web page의 특징을 간단하게 서술하시오.

- **Static Web Page**

  Static Web Page는 접속할 때마다 항상 같은 응답을 보내는 페이지이다. 기존에 만들어 둔 파일을 수정없이 보여주므로, 회사소개 페이지나 개인 소개 페이지에 적합하다.

- **Dynamic Web Page**

  Dynamic Web Page는 요청을 받으면 서버에서 추가적인 처리 과정을 거친 뒤 응답을 보낸다. 방문자와 상호작용하기 때문에 페이지 내용은 그때그때 다로다. 댓글, 날씨, 주가 정보와 같은 곳에 자주 사용된다. 



