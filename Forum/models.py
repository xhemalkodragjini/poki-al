from django.db import models
from django.contrib.auth import settings


class Post(models.Model):
    titulli = models.CharField(max_length=250)
    autori = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='post_author')
    teksti = models.TextField()
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulli


class Comment(models.Model):
    autori = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='comment_author')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    komenti = models.TextField()
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.komenti
