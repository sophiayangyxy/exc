from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from datetime import datetime
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from main.models import Post
from main.forms import NewPostForm, AnotherPostForm

# Create your views here.
def index(request):
    posts = Post.objects.order_by('-pk')
    context = {'posts': posts}
    return render(request, 'index.html', context)

def detail(request, post_pk):
    post = Post.objects.get(pk = post_pk)
    return render(request, 'detail.html', {'post': post})

def new(request):
    if request.method == 'GET':
        form = NewPostForm()
    else:
        form = NewPostForm(request.POST)
        if form.is_valid():
            new_title = form.cleaned_data['title']
            new_body = form.cleaned_data['body']
            new_time = datetime.now()
            p = Post.objects.create(title=new_title, body=new_body, post_time=new_time)
            p.save()
            return HttpResponseRedirect(reverse('detail', kwargs={'post_pk': p.id}))
    return render(request, 'new.html', {'form': form})

# @login_required
def delete(request, post_pk):
    Post.objects.filter(pk = post_pk).delete()
    posts = Post.objects.order_by('-pk')
    context = {'posts': posts}
    return render(request, 'index.html', context)

def edit(request, post_pk):
    p = Post.objects.get(pk = post_pk)
    if request.method == 'GET':
        form = AnotherPostForm(instance = p)
    else:
        form = AnotherPostForm(request.POST, instance = p)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('detail'), kwargs={'post_pk': p.id})
    return render(request, 'new.html', {'form': form})

# def my_view(request):
#     username = request.POST['username']
#     password = request.POST['password']
#     user = authenticate(username = username, password = password)
#     if user is not None:
#         if user.is_active:
#             login(request, user)
#     return HttpResponse('You have logged in')
#
# def logout_view(request):
#     logout(request)
#     return HttpResponse('You have logged out')


