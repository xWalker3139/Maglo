# Generated by Django 3.1.5 on 2021-12-11 20:49

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('my_app', '0038_anuntadult_favorit'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anuntadult',
            name='favorit',
            field=models.ManyToManyField(blank=True, related_name='favorit', to=settings.AUTH_USER_MODEL),
        ),
    ]
