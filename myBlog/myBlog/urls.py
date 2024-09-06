"""
URL configuration for myBlog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from users import views as users_view
from blog import views as blog_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login', users_view.login, name='login'),
    path('', blog_view.home, name='home'),
    path('logout', users_view.logout, name='logout'),
    path('register', users_view.register, name='register'),
    path('index', blog_view.index, name='index'),
    path('article/<int:id>', blog_view.article_detail, name='article_detail')
]
