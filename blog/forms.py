from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title','author','body']

#ModelPost의 fields중에서 사용자가 직접 데이터를 입력, 전송하는 fields를 밝혀준다.