# Generated by Django 3.1.5 on 2021-12-04 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0032_auto_20211204_1211'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anuntadult',
            name='titlul',
            field=models.CharField(max_length=264, null=True),
        ),
    ]