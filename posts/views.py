from django.shortcuts import render
from django.http import HttpResponse
from posts.models import Post
from posts.forms import PostForm
from django.contrib.auth.decorators import login_required



# Create your views here.
def post_view(request):
    if request.method == 'GET':
        posts = Post.objects.all()
        return render(request=request, template_name='post/post_list.html', context={'posts': posts})


def text_view(request):
    if request.method == 'GET':
        return HttpResponse("Это вьюшка текста")


def post_detail_view(request, post_id):
    if request.method == 'GET':
        post = Post.objects.get(id=post_id)
        return render(request,'post/post_detail_view.html', {'post':post})

def post_create_view(request):
    if request.method == 'GET':
        form = PostForm()
        return render(request,'post/post_create.html',{'form':form})
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if not form.is_valid():
            return render(request,'post/post_create.html',{'form':form})
        title = form.cleaned_data("title")
        content = form.cleaned_data("content")
        image = form.cleaned_data("image")
        post = Post.objects.filter(title=title,content=content)
        if not post:
            Post.objects.create(title=title, content=content, image=image)
            return HttpResponse("Пост создан")
        return HttpResponse("Такой пост уже существует")


@login_required(login_url='login')
def main_page(request):
    if request.method == 'GET':
        return render(request, "index.html")

