# Generated by Django 3.1.5 on 2022-01-11 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='anuntadult',
            name='caroserie',
            field=models.CharField(max_length=264, null=True),
        ),
    ]