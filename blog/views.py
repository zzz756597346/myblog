from django.shortcuts import render
from django.http import HttpResponse
import datetime
from . import models


def index(request):
    articles = models.Article.objects.all()
    return render(request, 'blog/index.html', {'articles': articles})


def article_page(request, article_id):
    article = models.Article.objects.get(pk=article_id)
    return render(request, 'blog/article_page.html', {'article': article})


def edit_page(request, article_id):
    if str(article_id) == '0':
        return render(request, 'blog/edit_page.html')
    article = models.Article.objects.get(pk=article_id)
    return render(request, 'blog/edit_page.html', {'article': article})


def edit_action(request):
    article_id = request.POST.get('article_id', '0')
    print('=' * 30)
    print(article_id)
    print('=' * 30)
    title = request.POST.get('title', 'TITLE')
    content = request.POST.get('content', 'CONTENT')

    pub_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    if article_id == '0':
        models.Article.objects.create(title=title, content=content, pub_time=pub_time)
        articles = models.Article.objects.all()
        return render(request, 'blog/index.html', {'articles': articles})
    else:
        article = models.Article.objects.get(pk=article_id)
        article.title = title
        article.content = content
        article.save()
        return render(request, 'blog/article_page.html', {'article': article})


def del_action(request):
    article_id = request.POST.get('article_id')
    print('=' * 30)
    print(article_id)
    print('=' * 30)
    models.Article.objects.filter(id=article_id).delete()
    articles = models.Article.objects.all()
    return render(request, 'blog/index.html', {'articles': articles})
