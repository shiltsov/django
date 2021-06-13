# Generated by Django 3.2.4 on 2021-06-13 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='название')),
                ('description', models.TextField(verbose_name='описание')),
                ('image', models.ImageField(upload_to='images', verbose_name='изображение')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'проект',
                'verbose_name_plural': 'проекты',
                'ordering': ['-created'],
            },
        ),
    ]
