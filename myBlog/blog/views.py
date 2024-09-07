from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib.auth.decorators import login_required
from users.models import User
from blog.models import Article, Comment
from django.core.paginator import Paginator
from django.db.models import Q
from .utility import *
from .forms import ArticleForm, CommentForm
from datetime import date
# Create your views here.

def home(request):
    if not is_user(request):
        return redirect(f"{settings.LOGIN_URL}")
    admin = is_admin(request)
    title = request.GET.get('title')
    kwargs = {'title__icontains': title}
    articles = Article.objects.all()
    articles = Article.objects.filter(Q(**kwargs)).distinct() if title else articles
    paginator = Paginator(articles, 2)
    page_number = request.GET.get("page")
    articles = paginator.get_page(page_number)
    return render(request, 'home.html', {'articles':articles, 'is_admin':admin})

def article_detail(request, id):
    if not is_user(request):
        return redirect(f"{settings.LOGIN_URL}")
    article = Article.objects.get(pk=id)
    if request.method == 'GET':
        form = CommentForm()
        article.view += 1
        article.save()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        content = form['content'].value()
        comment = Comment(content=content, article=article, send_user=User.objects.get(pk=request.session.get('user_id')))
        comment.save()
        form = CommentForm()
    comments = Comment.objects.filter(article=article)
    paginator = Paginator(comments, 3)
    page_number = request.GET.get("page")
    comments = paginator.get_page(page_number)
    return render(request, 'read_article.html', {'article':article, 'comments':comments, 'form':form})

def add_article(request):
    if not is_admin(request):
        return redirect(f"{settings.LOGIN_URL}")
    if request.method == 'GET':
        form = ArticleForm()
    else:
        form = ArticleForm(request.POST)
        if form.is_valid():
            title = form['title'].value()
            content = form['content'].value()
            article = Article(title=title, content=content, date=date.today(), wirter=User.objects.get(pk=request.session.get('user_id')))
            article.save()
            return redirect('home')
    return render(request, 'ArticleForm.html', {'form':form})
     
def update_article(request, id):
    if not is_admin(request):
        return redirect(f"{settings.LOGIN_URL}")
    article = Article.objects.get(pk=id)
    if request.method == 'GET':
        form = ArticleForm(instance=article)
    else:
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            article.title = form['title'].value()
            article.content = form['content'].value()
            article.save()
            return redirect('home')
    return render(request, 'ArticleForm.html', {'form':form})


def delete_article(request, id):
    if not is_admin(request):
        return redirect(f"{settings.LOGIN_URL}")
    article = Article.objects.get(pk=id)
    if request.method == 'GET':
        return render(request, 'delete.html', {'article':article})
    if request.method == 'POST':
        article.delete()
        return redirect('home')
    
