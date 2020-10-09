# 💻 PJT 06

## 1. 프로젝트 주제

영화 커뮤니티 서비스 게시판 기능 개발 (데이터베이스 설계)

<br>

## 2. 프로젝트 목표 

- 데이터를 생성, 조회, 수정, 삭제 할 수 있는 Web Application 제작
- Python Web Framework를 통한 데이터 조작
- Authentication에 대한 이해
- Database 1:N, M:N 관계의 이해와 데이터 관계 설정

<br>

## 3. 준비사항

- 언어
  -  Python 3.7+
  -  Django 3.X
- 도구
  -  vsCode
  -  Chrome Browser

<br>

## 4. 프로젝트 진행과정

### 4-0. 모델 생성

✔ 아래 설계도를 따라 모델을 생성한다.

![image-20201008132900031](README.assets/image-20201008132900031.png)

✔ User 모델과 Review 모델에  M:N 관계를 위한 필드를 추가해준다.

```python
# User 모델에 follower 필드를 추가한다.
follower = models.ManyToManyField('self', symmetrical=False, related_name='followings')
```

```python
# Review 모델에 like_users 필드를 추가한다.

like_users = models.ManyToManyField(settings.AUTH_USER_MODEL,related_name='like_reviews') 
```

<br>

---

<br>

### 4-1. CRUD

>  `pjt05` 에서 추가 기능 (사용자 정보, 팔로우, 좋아요) 을 추가해준다.
>

✔ **User**  `profile `  `follow`  기능 구현 (`accounts/view.py`)

```python
# 프로필
def profile(request, user_id):
    user = get_object_or_404(get_user_model(), pk=user_id)

    context = {
        'user':user,
    }
    return render(request, 'accounts/profile.html', context)


# 팔로우
@require_POST
@login_required
def follow(request, user_id):
    you = get_object_or_404(get_user_model(), pk=user_id)
    me = request.user
    if me != you:
        if me in you.follower.all():
            # 언팔
            you.follower.remove(me)
        else:
            # 팔로우
            you.follower.add(me)
    
    return redirect('accounts:profile', user_id)
```

✔  user 프로필 페이지

- 팔로우 X

![image-20201008135453995](README.assets/image-20201008135453995.png)

- 팔로우 O

![image-20201008135519183](README.assets/image-20201008135519183.png)

<br>

✔ **Review**  `like` 기능 구현 (`community/view.py`)

```python
@require_POST
def like(request, review_pk):
    if request.user.is_authenticated:
        review = get_object_or_404(Review, pk=review_pk)
        if review.like_users.filter(pk=request.user.pk).exists():
            review.like_users.remove(request.user)
        else:
            review.like_users.add(request.user)
        return redirect('community:index')
    return redirect('accounts:login')
```

![image-20201008135640583](README.assets/image-20201008135640583.png)

<br>

----

<br>

### 4. 추가 기능

(예정)

<br>

----



### 5. 정리

😉 팀원(재윤님)과 함께 빠르게 추가 기능을 마무리하고 헷갈린 부분도 복습할 수 있었다.

😉 모델폼을 커스터마이징하는 법을 어느정도 익힌 것 같다. 

✨  메인페이지, 기타 스타일링 마무리하기

