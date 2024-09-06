from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib.auth.decorators import login_required
from users.models import User
from blog.models import Article
from django.core.paginator import Paginator
from django.db.models import Q
# Create your views here.

def home(request):
    user_id = request.session.get('user_id')
    if not user_id:
        return redirect(f"{settings.LOGIN_URL}")
    title = request.GET.get('title')
    kwargs = {'title__icontains': title}
    articles = Article.objects.all()
    articles = Article.objects.filter(Q(**kwargs)).distinct() if title else articles
    paginator = Paginator(articles, 3)
    page_number = request.GET.get("page")
    articles = paginator.get_page(page_number)
    return render(request, 'home.html', {'articles':articles})

def index(request):
    user_id = request.session.get('user_id')
    if not user_id:
        return redirect(f"{settings.LOGIN_URL}")
    user = User.objects.get(pk=user_id)
    if not user.is_Admin:
        return redirect(f"{settings.LOGIN_URL}")
    articles = Article.objects.all()
    return render(request, 'index.html', {'articles':articles})

def article_detail(request, id):
    user_id = request.session.get('user_id')
    if not user_id:
        return redirect(f"{settings.LOGIN_URL}")
    article = Article.objects.get(pk=id)
    article.view += 1
    article.save()
    return render(request, 'read_article.html', {'article':article})
