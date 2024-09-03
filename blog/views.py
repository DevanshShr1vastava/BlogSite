from django.shortcuts import render, redirect
from .models import BlogPost, Category, Comment
from .forms import PostForm

# Create your views here.



from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .forms import PostForm, SignUpForm


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('blog_home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('blog_home')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})
    
   
def user_logout(request):
    logout(request)
    return redirect('blog_home')


def blog_home(request):
    posts = BlogPost.objects.all()
    return render(request, 'blog_home.html', {'posts': posts})

@login_required
def post_detail(request, post_id):
    post = BlogPost.objects.get(id=post_id)
    return render(request, 'post_detail.html', {'post': post})

@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog_home')  # Redirect to the homepage after saving
    else:
        form = PostForm()
    
    return render(request, 'create_post.html', {'form': form})