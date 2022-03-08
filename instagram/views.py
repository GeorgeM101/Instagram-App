from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from .models import Profile, Post,  Comment

# Create your views here.
def home(request):
    return render(request, 'index.html')


def register(request):
    if request.method == 'POST':
        first_name = request.POST['firstname']
        last_name = request.POST['lastname']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        if User.objects.filter(username=username).exists():
            messages.info(request,'Username already taken!')
            return redirect('register')
        elif User.objects.filter(email=email).exists():
            messages.info(request,'Email already exists!')
            return redirect('register')
        else:
            user = User.objects.create_user(username=username,password=password,email=email,first_name=first_name,last_name=last_name)
            user.save()
            print('user created')
            return redirect('login')
    return render(request,'register.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'Invalid Credentials')
            return redirect('login')
    else:
        return render(request,'login.html')

def index(request):
    current_user = request.user
    if request.method == 'POST':
        image = request.FILES.get('image')
        name = request.POST['name']
        caption = request.POST['caption']

        new_post = Post(user=current_user,picture=image,title=name,caption=caption,profile=current_user.profile)
        new_post.save()
    posts = Post.objects.all()
    user = User.objects.all()
    return render(request,'index.html',{'posts':posts,'user':user,'current_user':current_user})

def search_results(request):

    if 'article' in request.GET and request.GET["post"]:
        search_term = request.GET.get("post")
        searched_posts = Post.search_by_title(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"posts": searched_posts})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})
        
def logout(request):
    auth.logout(request)
    return redirect('login')
