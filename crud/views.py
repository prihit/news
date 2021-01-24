from django.shortcuts import render, redirect, get_object_or_404
from crud.models import News
from django.contrib import messages, auth
from django.contrib.auth.models import User
# Create your views here.


def index(request):
    news= News.objects.all()
    context = {
        'news': news
    }
    return render(request, 'index.html', context)

def register(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email has been taken up before')
            return redirect('/register')
        else:
            user = User.objects.create_user(username=email,email=email,password=password)
            auth.login(request, user)
            messages.success(request, 'you are logged in')
            return redirect('/news')
    else:
        return render(request, 'register.html')

def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = auth.authenticate(username=email, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/news')
        else:
            messages.error(request, 'Invalid Email')
            return redirect('/login')
    else:
        return render(request, 'login.html')

def logut(request):
    auth.logout(request)
    return redirect('/login')


def createnews(request):
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        location = request.POST['location']
        author = request.user.email
        news = News.objects.create(title=title,location=location,description=description,image=image,author=author)
        news.save()
        return redirect('/news')
    else:
        return render(request, 'newsform.html')

def shownews(request, id):
    news = get_object_or_404(News, pk=id)
    context={
        'news': news
    }
    return render(request, 'news.html', context)

def updatenews(request, id):
    news = get_object_or_404(News, pk=id)
    if request.method== 'POST':
        title = request.POST['title']
        description = request.POST['description']
        location = request.POST['location']
        author = request.user.email
        news.title = title
        news.description = description
        news.location = location
        news.author = author
        news.save()
        return redirect('/news')
    else:
        if request.user.email == news.author:
            context = {
                'news': news
            }
            return render(request, 'updatenews.html',context)
        else:
            return render(request, "error.html")


def deletenews(request, id):
    news = get_object_or_404(News, pk=id)
    if request.user.email == news.author:
        news.delete()
        return redirect("/news")
    else:
        return render(request, "error.html")
