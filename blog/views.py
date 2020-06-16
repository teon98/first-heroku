from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from .forms import PostForm # forms.py에서 PostForm 가져오기

# Create your views here.
def main(request):
    posts = Post.objects # Post.objects를 posts 변수에 담기
    return render(request, 'posts.html', {'posts':posts}) #인자 3개 : request, template, context

def create(request):
    if request.method == 'POST': #POST vs. GET분기
        form = PostForm(request.POST) # form 변수에 PostForm 할당
        if form.is_valid(): # form 유효성 검증
            form.save() #저장하고
            return redirect('main') # main 페이지로 가기
    else:
        form = PostForm() # 빈 form 열기
    
    return render(request, 'create.html', {'form':form})

def detail(request, pk): #request와 pk(primary key)도 인자로 받음
    post = get_object_or_404(Post, pk=pk) # 해당 객체가 있으면 가져오고 없으면 404에러, pk로 pk 사용
    return render(request, 'detail.html', {'post':post})

def update(request, pk): #특정 게시물을 골라내기 위해 pk값을 받아옴
    post = get_object_or_404(Post, pk=pk) 
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post) # post 객체 가져오기
        if form.is_valid():
            form.save()
            return redirect('main')
    else:
        form = PostForm(instance=post) # post 객체 가져와서 form 생성

        return render(request, 'update.html', {'form':form})

def delete(request, pk):
    post = Post.objects.get(pk=pk)
    post.delete()
    return redirect('main')