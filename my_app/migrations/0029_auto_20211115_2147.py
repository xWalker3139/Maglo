# Generated by Django 3.1.5 on 2021-11-15 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0028_auto_20211115_2136'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='copil',
            name='user',
        ),
        migrations.AddField(
            model_name='copil',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='copil',
            name='nume',
            field=models.CharField(max_length=264, null=True),
        ),
        migrations.AddField(
            model_name='copil',
            name='parola',
            field=models.CharField(max_length=264, null=True),
        ),
        migrations.AddField(
            model_name='copil',
            name='prenume',
            field=models.CharField(max_length=264, null=True),
        ),
    ]