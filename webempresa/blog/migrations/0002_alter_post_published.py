# Generated by Django 3.2.4 on 2021-06-27 13:48

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='published',
            field=models.DateTimeField(default=datetime.datetime(2021, 6, 27, 13, 48, 47, 571154, tzinfo=utc)),
        ),
    ]
