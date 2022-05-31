from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path("articles/", views.articles, name="articles"),
    path("articles/<int:article_id>/", views.article, name="articleView"),
    path("user_detail/<str:nickname>/", views.user, name="userView")
]
