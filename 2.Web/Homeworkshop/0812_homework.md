# 0812_homework

### 1.  Buttons

```html
<!-- w-50 == Width 50% -->
<button type="button" class="btn btn-success w-50">Sign in</button>
```



---



### 2. Navbar

```html
<!-- Color schemes -->
<nav class="navbar navbar-expand-lg navbar-dark bg-dark">
            
	<!-- SSAFY 로고 삽입 -->
	<a class="navbar-brand" href="#">
        <img src="https://www.ssafy.com/swp_m/images/common/logo3.png" alt="ssafy logo" width="50">
    </a>
      
    <div class="collapse navbar-collapse" id="navbarSupportedContent">
        <ul class="navbar-nav mr-auto">

            <!-- Dropdown menu (프로젝트, 그룹들, 더보기) 만들기 -->
            <li class="nav-item dropdown">
                <a class="nav-link dropdown-toggle text-white" href="#" id="navbarDropdown" role="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                    프로젝트
                </a>
                <div class="dropdown-menu" aria-labelledby="navbarDropdown">
                    <a class="dropdown-item" href="#">Action</a>
                    <a class="dropdown-item" href="#">Another action</a>
                    <div class="dropdown-divider"></div>
                    <a class="dropdown-item" href="#">Something else here</a>
                </div>
            </li>
            
            <li class="nav-item dropdown">
                <a class="nav-link dropdown-toggle text-white" href="#" id="navbarDropdown" role="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                    그룹들
                </a>
                <div class="dropdown-menu" aria-labelledby="navbarDropdown">
                    <a class="dropdown-item" href="#">Action</a>
                    <a class="dropdown-item" href="#">Another action</a>
                    <div class="dropdown-divider"></div>
                    <a class="dropdown-item" href="#">Something else here</a>
                </div>
            </li>

            <li class="nav-item dropdown">
                <a class="nav-link dropdown-toggle text-white" href="#" id="navbarDropdown" role="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                    더보기
                </a>
                <div class="dropdown-menu" aria-labelledby="navbarDropdown">
                    <a class="dropdown-item" href="#">Action</a>
                    <a class="dropdown-item" href="#">Another action</a>
                    <div class="dropdown-divider"></div>
                    <a class="dropdown-item" href="#">Something else here</a>
                </div>
            </li>
            
        </ul>
    </div>
</nav>
```



---



### 3. Pagination

```html
<nav aria-label="Page navigation example">
    <ul class="pagination">
        <li class="page-item">
            <a class="page-link text-dark" href="#" aria-label="Previous">
                PREV
            </a>
        </li>
        <li class="page-item"><a class="page-link text-dark" href="#">1</a></li>
        <li class="page-item"><a class="page-link text-dark" href="#">2</a></li>
        <li class="page-item"><a class="page-link text-dark" href="#">3</a></li>
        <li class="page-item"><a class="page-link text-dark" href="#">4</a></li>
        <li class="page-item"><a class="page-link text-dark" href="#">5</a></li>
        <li class="page-item"><a class="page-link text-dark" href="#">...</a></li>
        <li class="page-item">
            <a class="page-link text-dark" href="#" aria-label="Next">
                NEXT
            </a>
        </li>
        <li class="page-item">
            <a class="page-link text-dark" href="#" aria-label="Next">
                <span aria-hidden="true">&raquo;</span>
            </a>
        </li>
    </ul>
</nav>
```



---



### 4. Login Page

```html
<div class="alert alert-danger" role="alert">
    Invalid Login or Password.
</div>

<h1>SSAFY 전용 GitLab 시스템</h1>
<form class="p-3 border">
    <h5 class="text-center font-weight-bold">Sign in</h5>
    <hr class="bg-primary">

    <div class="form-group">
        <label for="exampleInputEmail1" class="font-weight-bold">Username or email</label>
        <input type="email" class="form-control" id="exampleInputEmail1" aria-describedby="emailHelp">
    </div>
    <div class="form-group">
        <label for="exampleInputPassword1" class="font-weight-bold">Password</label>
        <input type="password" class="form-control" id="exampleInputPassword1">
    </div>

    <!-- remember me 와 forgot your password를 flex 레이아웃으로 정렬한다. -->
    <div class="d-flex justify-content-between">
        <div class="form-group form-check">
            <input type="checkbox" class="form-check-input" id="exampleCheck1">
            <label class="form-check-label" for="exampleCheck1">Remember me</label>
        </div>
        <a href="#">Forgot your password?</a>
    </div>
    <button type="submit" class="btn btn-success w-100">Sign in</button>
</form>
```











































