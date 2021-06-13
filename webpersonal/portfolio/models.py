from django.db import models

# Create your models here.


class Project(models.Model):
    title = models.CharField(max_length=200, verbose_name='название')
    description = models.TextField(verbose_name='описание')
    image = models.ImageField(upload_to='images', verbose_name='изображение')
    link = models.URLField(max_length=200, null=True,
                           blank=True, verbose_name='ссылка')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'проект'
        verbose_name_plural = 'проекты'
        ordering = ['-created']
