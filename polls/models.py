from django.db import models


class User(models.Model):
    email = models.EmailField()
    password = models.CharField(max_length=50)
    nickname = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.nickname} - {self.email}"


class Article(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    pub_date = models.DateTimeField(auto_now_add=True)
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} - {self.author} ({self.pub_date}): \n\n{self.content}"


class Comment(models.Model):
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    pub_date = models.DateTimeField(auto_now_add=True)
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.author}'s comment on {self.article}: \n\n{self.content}"
