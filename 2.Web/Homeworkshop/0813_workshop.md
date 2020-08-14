# 0813_workshop

### 1. 기본 그리드 레이아웃 (01_grid.html)

`col-n` : 총 12칸 중에서 n칸을 차지한다는 뜻.

```html
<!-- 1. -->
<div class="row">
    <div class="col-4 item">
        <p>4개</p>
    </div>
    <div class="col-4 item">
        <p>4개</p>
    </div>
    <div class="col-4 item">
        <p>4개</p>
    </div>
</div>	

<!-- 2. -->
<div class="row">
    <div class="item col-6">
        <p>6개</p>
    </div>
    <div class="item col-6">
        <p>6개</p>
    </div>   
</div>

<!-- 3. -->
<div class="row">
    <div class="item col-3">
        <p>3개</p>
    </div>  
    <div class="item col-6">
        <p>6개</p>
    </div>
    <div class="item col-3">
        <p>3개</p>
    </div>
</div>

<!-- 4. -->
<div class="row">
    <div class="item col-2">
        <p>2개</p>
    </div>
    <div class="item col-7">
        <p>7개</p>
    </div>
    <div class="item col-3">
        <p>3개</p>
    </div> 
</div>
```



---

### 2. 반응형 그리드

`-sm` : ~576px

`-md` : 576~768px

`-lg` : 768~992px

`-xl` : 1200px~

```html
<!-- 1. -->
<div class="row">
    <div class="item col-4 col-sm-2">
        <p>576px 미만 4 <br> 576px 이상 2</p>
    </div>
    <div class="item col-4 col-sm-5">
        <p>576px 미만 4 <br> 576px 이상 5</p>
    </div>
    <div class="item col-4 col-sm-5">
        <p>576px 미만 4 <br> 576px 이상 5</p>
    </div>
</div>

<!-- 2. -->
<div class="row">
    <div class="item col-sm-1 col-md-2">
        <p>768px 미만 1 <br> 768px 이상 2</p>
    </div>
    <div class="item col-sm-3 col-md-3">
        <p>768px 미만 3 <br> 768px 이상 3</p>
    </div>
    <div class="item col-sm-4 col-md-3">
        <p>768px 미만 4 <br> 768px 이상 3</p>
    </div>
    <div class="item col-sm-1 col-md-2">
        <p>768px 미만 1 <br> 768px 이상 2</p>
    </div>
    <div class="item col-sm-3 col-md-2">
        <p>768px 미만 3 <br> 768px 이상 2</p>
    </div>
</div>

<!-- 3. -->
<div class="row">
    <div class="item col-4 col-sm-3 col-md-6">
        <p>576px 미만 4 <br> 768px 미만 3 <br> 768px 이상 6</p>
    </div>
    <div class="item col-6 col-sm-3 col-md-6">
        <p>576px 미만 6 <br> 768px 미만 3 <br> 768px 이상 6</p>
    </div>
    <div class="item col-2 col-sm-6 col-md-12">
        <p>576px 미만 2 <br> 768px 미만 6 <br> 768px 이상 12</p>
    </div>
</div>

<!-- 4. -->
<div class="row">
    <div class="item col-sm-12 col-md-4 col-xl-2">
        <p>768px 미만 12 <br> 768px 이상 4 <br> 1200px 이상 2</p>
    </div>
    <div class="item col-sm-12 col-md-4 col-xl-2">
        <p>768px 미만 12 <br> 768px 이상 4 <br> 1200px 이상 2</p>
    </div>
    <div class="item col-sm-12 col-md-4 col-xl-12">
        <p>768px 미만 12 <br> 768px 이상 4 <br> 1200px 이상 12</p>
    </div>
</div>
```



---

### 3. 그리드 심화

`offset-n` : 앞에 n만큼 공백을 준다.

```html
<!-- 1. -->
<div class="row">
    <div class="item col-sm-4 col-md-4">
        <p>item1</p>
    </div>
    <div class="item col-sm-8 col-md-4 offset-md-4">
        <p>item2</p>
    </div>
</div>

<!-- 2. -->
<div class="row">
    <div class="item col-sm-4 col-md-4 offset-md-4 col-lg-5 offset-lg-7">
        <p>item1</p>
    </div>
    <div class="item col-sm-4 offset-sm-4 col-md-4 offset-md-0 col-lg-8 offset-lg-2 ">
        <p>item2</p>
    </div>
</div>


<!-- 3. -->
<div class="row">
    <div class="item col-sm-12 col-md-3">
        item1
    </div>
    <div class="item col-sm-12 col-md-9">
        <div class="row">
            <div class="item col-sm-6 col-lg-3">item2</div>
            <div class="item col-sm-6 col-lg-3">item3</div>
            <div class="item col-sm-6 col-lg-3">item4</div>
            <div class="item col-sm-6 col-lg-3">item5</div>
        </div>
    </div>
</div>
```

