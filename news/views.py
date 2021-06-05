from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect
from .models import News, Category, Rating
from .forms import NewNewsForm, RegisterForm, LoginForm, RatingForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

from django.shortcuts import render, redirect, get_object_or_404
from django.views import View


def index(request):
    news = News.objects.all()
    content = {
        'news': news,
        'title': 'Список новостей',
    }
    return render(request, 'news/index.html', content)


def user(request, pk):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/login')

    my_user = get_object_or_404(User, id=pk)
    news = News.objects.filter(owner=pk)
    context = {
        'user': my_user,
        'news': news,
    }
    return render(request, 'news/user.html', context)


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(form.cleaned_data['username'],
                                            form.cleaned_data['email'],
                                            form.cleaned_data['password'])
            user.last_name = form.cleaned_data['lastName']
            user.first_name = form.cleaned_data['firstName']
            user.save()
    else:
        form = RegisterForm()

    return render(request, 'news/register.html', {'form': form})


def login_user(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'],
                                password=form.cleaned_data['password'])
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/')
    else:
        form = LoginForm()

    return render(request, 'news/login.html', {'form': form})


def view_by_category(request, category_id):
    news = News.objects.filter(category_id=category_id)
    category = Category.objects.get(pk=category_id)

    return render(request, 'news/view_by_category.html', {'news': news, 'category': category,
                                                  },)


def add_news(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/login')

    fix_me = ""

    if request.method == 'POST':
        form = NewNewsForm(request.POST)
        if form.is_valid():
            news = News()
            news.owner = request.user
            news.title = form.cleaned_data['title']
            news.content = form.cleaned_data['content']
            news.save()
            fix_me = "Запись успешно добавлена"
    else:
        form = NewNewsForm
    return render(request, 'news/add_news.html', {'form': form, 'msg': fix_me})


def view_news(request, news_id):
    news_item = get_object_or_404(News, pk=news_id)
    return render(request, 'news/view_news.html', {'news_item': news_item})


def error_404(request, exception):
    return render(request, 'blog/404.html')

def search(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/login')

    query = request.GET.get('query')
    if request.GET.get('query') is None:
        return render(request, 'news/index.html')

    res = News.objects.filter(Q(title__icontains=request.GET.get('query')) |
                              Q(clipped_text__icontains=request.GET.get('query')) |
                              Q(text__icontains=request.GET.get('query')))
    return render(request, 'news/search.html', {'result': res})


def rate_news(request, pk):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/login')

    news = get_object_or_404(News, id=pk)

    if request.method == 'POST':
        form = RatingForm(request.POST)
        if form.is_valid():
            try:
                r = Rating(owner=request.user, news=news)
                r.save()
                news.rating_sum = news.rating_sum + form.cleaned_data['rating_sum']
                news.save()
            except BaseException as e:
                pass
    return HttpResponseRedirect(f'/view_news/{pk}/')









