# Generated by Django 3.1.5 on 2021-11-17 19:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('my_app', '0029_auto_20211115_2147'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='adult',
            name='email',
        ),
        migrations.RemoveField(
            model_name='adult',
            name='prenume',
        ),
        migrations.AddField(
            model_name='adult',
            name='emailul',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='adult',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='adult',
            name='nume',
            field=models.CharField(max_length=264, null=True),
        ),
        migrations.AlterField(
            model_name='adult',
            name='parola',
            field=models.CharField(max_length=264, null=True),
        ),
    ]