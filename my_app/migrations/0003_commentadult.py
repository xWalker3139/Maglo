# Generated by Django 3.1.5 on 2022-03-19 09:58

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0002_auto_20220124_2147'),
    ]

    operations = [
        migrations.CreateModel(
            name='CommentAdult',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nume', models.CharField(max_length=264, null=True)),
                ('prenume', models.CharField(max_length=264, null=True)),
                ('comment', models.TextField(max_length=100000, null=True)),
                ('date', models.DateTimeField(default=datetime.datetime(2022, 3, 19, 11, 58, 11, 458036), null=True)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='my_app.anuntadult')),
            ],
        ),
    ]