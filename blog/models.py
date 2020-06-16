from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=100) #제목
    author = models.CharField(max_length=20) #글쓴이
    body = models.TextField() #본문
    date = models.DateTimeField(auto_now_add=True) #auto_now_add = 마지막으로 수정한 날짜를 올려줌

    def __str__(self):
        return self.title
    