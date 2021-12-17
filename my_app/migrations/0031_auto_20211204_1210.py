# Generated by Django 3.1.5 on 2021-12-04 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0030_auto_20211117_2148'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anuntadult',
            name='categorie_adult',
            field=models.CharField(choices=[('Auto, moto si ambarcatiuni', 'Auto, moto si ambarcatiuni'), ('Piese auto', 'Piese auto'), ('Agro si industrie', 'Agro si industrie'), ('Imobiliare', 'Imobiliare'), ('Moda si frumusete', 'Moda si frumusete'), ('Electronice si electrocasnice', 'Electronice si electrocasnice'), ('Afaceri/Servicii', 'Afaceri/Servicii'), ('Animale de companie', 'Animale de companie'), ('Locuri de munca', 'Locuri de munca'), ('Sport, timp liber si Hobby', 'Sport, timp liber si Hobby')], max_length=264),
        ),
        migrations.AlterField(
            model_name='anuntadult',
            name='titlul',
            field=models.CharField(default=None, max_length=264, null=True),
        ),
    ]