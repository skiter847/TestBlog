from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
from django.urls import reverse


# Create your models here.
class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор')
    photo_title = models.ImageField(upload_to='title/', verbose_name='Титульное фото', blank=True)
    title = models.CharField(max_length=200, verbose_name='Заглавие')
    slug = models.SlugField(max_length=200)
    body = models.TextField(verbose_name='Текст')
    publish = models.DateTimeField(default=now, verbose_name='Дата публикации')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse("blog:post_detail", args=[self.id])

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-publish']
