from typing import ContextManager
from django.db import models

# Create your models here.

class Service(models.Model):
    title = models.CharField(max_length=200, verbose_name="заголовок")
    subtitle = models.CharField(max_length=200, verbose_name="подзаголовок")
    content = models.TextField(verbose_name="описание")
    image = models.ImageField(upload_to="images", verbose_name="изображение")
    created = models.DateTimeField(auto_now_add=True, verbose_name="дата создания")
    updated = models.DateTimeField(auto_now=True, verbose_name="дата изменения")

    def __str__(self):
        return self.title + "(" + "{:%d.%m.%Y}".format(self.created) + ")"

    class Meta:
        verbose_name = "сервис"
        verbose_name_plural = "сервисы"
        ordering = ["-created"]