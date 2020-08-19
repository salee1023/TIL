from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=10)
    content = models.TextField()
    # # 게시물 생성시간
    created_at = models.DateTimeField(auto_now_add=True)
    # # 마지막 수정 시간
    updated_at = models.DateTimeField(auto_now=True)

    # # 객체의 표현을 바꿔줌.
    def __str__(self):
        return self.title