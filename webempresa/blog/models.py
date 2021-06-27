from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='название')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'
        ordering = ['-name'] 

class Post(models.Model):
    title = models.CharField(max_length=100, verbose_name='заголовок')
    content = models.TextField(verbose_name='содержание')
    published = models.DateTimeField(default=now)
    image = models.ImageField(upload_to='images', verbose_name='изображение')
    author = models.ForeignKey(User, verbose_name='автор', on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category, verbose_name='категория')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title + ' (' + str(self.author) + ') '

    class Meta:
        verbose_name = 'запись'
        verbose_name_plural = 'записи'
        ordering = ['-published']