# Generated by Django 3.1.5 on 2021-12-11 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0034_auto_20211210_1814'),
    ]

    operations = [
        migrations.AddField(
            model_name='anuntadult',
            name='moneda',
            field=models.CharField(max_length=264, null=True),
        ),
        migrations.AlterField(
            model_name='anuntcopil',
            name='titlul',
            field=models.CharField(blank=True, max_length=264, null=True),
        ),
    ]
