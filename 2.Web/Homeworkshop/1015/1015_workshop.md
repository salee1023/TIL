# 1015_workshop

### 1. 좋아요 기능

```html
<!--좋아요 폼-->
<form class="d-inline like-form" data-article-id="{{ article.pk }}"> 
    {% csrf_token %}
    {% if request.user in article.like_users.all %}
    <button class="btn btn-link" style="color: crimson;">
        <i id="like-{{ article.pk }}" class="fas fa-heart"></i>
    </button>
    {% else %}
    <button class="btn btn-link" style="color: black;">
        <i id="like-{{ article.pk }}" class="fas fa-heart"></i>
    </button>
    {% endif %}
</form>

<!------------------------------------------------------------------------------->

<script src="https://cdn.jsdelivr.net/npm/axios/dist/axios.min.js"></script>
<script>
  // 페이지에 존재하는 모든 좋아요 폼(버튼) 선택 
  const likeForms = document.querySelectorAll('.like-form')
  const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value

  // 좋아요 폼 하나씩 꺼내서 처리
  likeForms.forEach(function (likeForm) {

    likeForm.addEventListener('submit', function (event) {
      event.preventDefault()
      const articleId = event.target.dataset.articleId
      axios.post(`http://127.0.0.1:8000/articles/${articleId}/like/`, {}, {
        headers: {'X-CSRFToken': csrftoken}
      })
        .then(function (res) {
          const liked = res.data.liked
          const likeCount = res.data.like_count

          const likeIcon = document.querySelector(`#like-${articleId}`)
          const likeCountSpan = document.querySelector(`#like-count-${articleId}`)
          
          likeCountSpan.innerText = likeCount
          likeIcon.style.color = liked ? 'crimson' : 'black'
        })
        .catch(function (err) {
          console.log(err)
        })
    })
  })
</script>
```

```python
@require_POST
def like(request, article_pk):
    if request.user.is_authenticated:
        article = get_object_or_404(Article, pk=article_pk)
        if article.like_users.filter(pk=request.user.pk).exists(): 
            article.like_users.remove(request.user)
            liked = False
        else:
            article.like_users.add(request.user)
            liked = True

        like_status = {
            'liked': liked,
            'like_count' : article.like_users.count(),
        }
        return JsonResponse(like_status)
        # return redirect('articles:index')
    return redirect('accounts:login')
```


---

### 2. 팔로우 기능

```html
<form class="follow-form" data-user-id="{{ person.pk }}">
        {% csrf_token %}
        {% if request.user in followers %}
          <button class="btn btn-secondary">Unfollow</button>
        {% else %}
          <button class="btn btn-primary">Follow</button>
        {% endif %}
      </form>

<!-------------------------------------------------------------------------------->

<script src="https://cdn.jsdelivr.net/npm/axios/dist/axios.min.js"></script>
<script>
const followForm = document.querySelector('.follow-form')
const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value

followForm.addEventListener('submit', function (event) {
  event.preventDefault()
  const userId = event.target.dataset.userId
  axios.post(`http://127.0.0.1:8000/accounts/${userId}/follow/`, {}, {
    headers: {'X-CSRFToken': csrftoken}
  })
    .then(function (res) {
      console.log(res)
      const follow = res.data.follow
      const followers = res.data.followers
      const followings = res.data.follwings

      const button = document.querySelector('button')
      const followerCnt = document.querySelector('#follower-count')
      const followingCnt = document.querySelector('#following-count')

      button.classList.toggle('btn-primary')
      button.classList.toggle('btn-secondary')

      button.innerText = follow ? 'unfollow' : 'follow'
      followerCnt.innerText = followers
      followingCnt.innerText = followings
    })
    .catch(function (err) {

    })
  
})
</script>
```

```python 
@require_POST
def follow(request, user_pk):
    # 상대방
    you = get_object_or_404(get_user_model(), pk=user_pk)
    # 나
    me = request.user

    if me != you:
        # if user in person.followers.all():
        if you.followers.filter(pk=me.pk).exists():
            you.followers.remove(me)
            follow = False
        else:
            you.followers.add(me)
            follow = True
            
    follow_status = {
        'follow': follow,
        'followers' : you.followers.count(),
        'followings' : you.followings.count(),
    }
    return JsonResponse(follow_status)
```





