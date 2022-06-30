from django.contrib.auth.models import User
from django.db import models

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

class Women(models.Model):
    title = models.CharField(max_length=255, verbose_name="Заголовок")
    content = models.TextField(blank=True, verbose_name="Текст статьи")
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")
    time_update = models.DateTimeField(auto_now=True, verbose_name="Время изменения")
    is_published = models.BooleanField(default=True, verbose_name="Публикация")
    author = models.ForeignKey('Profile', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
        ordering = ['-time_create', 'title']
