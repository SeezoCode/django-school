from django.http import HttpResponse
from django.template import loader

from .models import Article, User
from .models import Comment


def index(request):
    template = loader.get_template('polls/index.html')
    latest_articles = Article.objects.order_by('-timestamp')[:3]
    top_authors = User.objects.order_by('nickname')[:6]
    l = []
    for latest_article in latest_articles:
        latest_article.content = " ".join(latest_article.content.split(" ")[:12]) + "..."
        l.append(latest_article)
    context = {
        "latest_articles": l,
        "users": top_authors
    }
    return HttpResponse(template.render(context, request))


def articles(request):
    latest_articles = Article.objects.order_by('-timestamp')[:500]
    template = loader.get_template('polls/articles_view.html')
    context = {
        "latest_articles": latest_articles,
    }
    return HttpResponse(template.render(context, request))


def article(request, article_id):
    articleReq = Article.objects.get(id=article_id)
    commentReq = Comment.objects.filter(article=article_id).order_by("timestamp")

    template = loader.get_template("polls/article_view.html")
    context = {
        "article": articleReq,
        "comments": commentReq
    }
    return HttpResponse(template.render(context, request))


def user(request, nickname):
    user = User.objects.get(nickname=nickname)
    commentReq = Comment.objects.filter(author=user.id)
    articleReq = Article.objects.filter(author=user.id)

    template = loader.get_template('polls/user_view.html')
    context = {
        "user": user,
        "comments": commentReq,
        "articles": articleReq
    }
    return HttpResponse(template.render(context, request))
