# Generated by Django 3.1.5 on 2022-01-11 15:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Afacere',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titlul', models.CharField(max_length=264, null=True)),
                ('numele_firmei', models.CharField(max_length=264, null=True)),
                ('descriere', models.TextField(max_length=9000, null=True)),
                ('imagine', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('imagine2', models.ImageField(blank=True, null=True, unique=True, upload_to='images/')),
                ('imagine3', models.ImageField(blank=True, null=True, unique=True, upload_to='images/')),
                ('imagine4', models.ImageField(blank=True, null=True, unique=True, upload_to='images/')),
                ('imagine5', models.ImageField(blank=True, null=True, unique=True, upload_to='images/')),
                ('imagine6', models.ImageField(blank=True, null=True, unique=True, upload_to='images/')),
                ('judet', models.CharField(choices=[('Alba', 'Alba'), ('Arad', 'Arad'), ('Arges', 'Arges'), ('Bacau', 'Bacau'), ('Bihor', 'Bihor'), ('Bistrita-Nasaud', 'Bistrita-Nasaud'), ('Botosani', 'Botosani'), ('Braila', 'Braila'), ('Brasov', 'Brasov'), ('Buzau', 'Buzau'), ('Calarasi', 'Calarasi'), ('Caras-Severin', 'Caras-Severin'), ('Cluj', 'Cluj'), ('Constanta', 'Constanta'), ('Covasna', 'Covasna'), ('Dambovita', 'Dambovita'), ('Dolj', 'Dolj'), ('Galati', 'Galati'), ('Giurgiu', 'Giurgiu'), ('Gorj', 'Gorj'), ('Harghita', 'Harghita'), ('Hunedoara', 'Hunedoara'), ('Ialomita', 'Ialomita'), ('Iasi', 'Iasi'), ('Ilfov', 'Ilfov'), ('Maramures', 'Maramures'), ('Mehedinti', 'Mehedinti'), ('Mures', 'Mures'), ('Neamt', 'Neamt'), ('Olt', 'Olt'), ('Prahova', 'Prahova'), ('Salaj', 'Salaj'), ('Satu Mare', 'Satu Mare'), ('Sibiu', 'Sibiu'), ('Suceava', 'Suceava'), ('Teleorman', 'Teleorman'), ('Timis', 'Timis'), ('Tulcea', 'Tulcea'), ('Valcea', 'Valcea'), ('Vaslui', 'Vaslui'), ('Vrancea', 'Vrancea')], max_length=264)),
                ('adresa', models.CharField(max_length=264, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('telefon', models.IntegerField(blank=True, null=True)),
                ('tipul_afacerii', models.CharField(choices=[('Cabinet medical', 'Cabinet medical'), ('Cabinet psihologic', 'Cabinet psihologic'), ('Cafenea', 'Cafenea'), ('Cofetarie', 'Cofetarie'), ('Constructii', 'Constructii'), ('Frizerii', 'Frizerii'), ('Hotel', 'Hotel'), ('Fast-Food-uri', 'Fast-Food-uri'), ('Pensiune', 'Pensiune'), ('Restaurant', 'Restaurant'), ('Saloane de coafura', 'Saloane de coafura'), ('Service Auto', 'Service Auto')], max_length=264)),
            ],
        ),
        migrations.CreateModel(
            name='AjutorSiContact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nume', models.CharField(max_length=264)),
                ('email', models.EmailField(max_length=254)),
                ('descriere', models.TextField(max_length=9000)),
            ],
        ),
        migrations.CreateModel(
            name='AnuntCopil',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titlul', models.CharField(blank=True, max_length=264, null=True)),
                ('numele_anuntului', models.CharField(max_length=264, null=True)),
                ('descriere', models.TextField(max_length=9000)),
                ('categorie_copil', models.CharField(choices=[('Carti', 'Carti'), ('Jucarii', 'Jucarii'), ('Haine', 'Haine'), ('Articole sportive', 'Articole sportive'), ('Schimburi', 'Schimburi'), ('Mama si copil', 'Mama si copil')], max_length=264)),
                ('telefon', models.PositiveIntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('pret', models.FloatField(blank=True, null=True)),
                ('moneda', models.CharField(blank=True, max_length=264, null=True)),
                ('imagine', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('imagine2', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('imagine3', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('imagine4', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('imagine5', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('imagine6', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('localizare', models.CharField(choices=[('Alba', 'Alba'), ('Arad', 'Arad'), ('Arges', 'Arges'), ('Bacau', 'Bacau'), ('Bihor', 'Bihor'), ('Bistrita-Nasaud', 'Bistrita-Nasaud'), ('Botosani', 'Botosani'), ('Braila', 'Braila'), ('Brasov', 'Brasov'), ('Buzau', 'Buzau'), ('Calarasi', 'Calarasi'), ('Caras-Severin', 'Caras-Severin'), ('Cluj', 'Cluj'), ('Constanta', 'Constanta'), ('Covasna', 'Covasna'), ('Dambovita', 'Dambovita'), ('Dolj', 'Dolj'), ('Galati', 'Galati'), ('Giurgiu', 'Giurgiu'), ('Gorj', 'Gorj'), ('Harghita', 'Harghita'), ('Hunedoara', 'Hunedoara'), ('Ialomita', 'Ialomita'), ('Iasi', 'Iasi'), ('Ilfov', 'Ilfov'), ('Maramures', 'Maramures'), ('Mehedinti', 'Mehedinti'), ('Mures', 'Mures'), ('Neamt', 'Neamt'), ('Olt', 'Olt'), ('Prahova', 'Prahova'), ('Salaj', 'Salaj'), ('Satu Mare', 'Satu Mare'), ('Sibiu', 'Sibiu'), ('Suceava', 'Suceava'), ('Teleorman', 'Teleorman'), ('Timis', 'Timis'), ('Tulcea', 'Tulcea'), ('Valcea', 'Valcea'), ('Vaslui', 'Vaslui'), ('Vrancea', 'Vrancea')], max_length=264)),
            ],
        ),
        migrations.CreateModel(
            name='Copil',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nume', models.CharField(max_length=264, null=True)),
                ('prenume', models.CharField(max_length=264, null=True)),
                ('email', models.EmailField(max_length=254, null=True)),
                ('parola', models.CharField(max_length=264, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='MesajAdult',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mesaj', models.TextField(max_length=9000)),
            ],
        ),
        migrations.CreateModel(
            name='MesajAfaceri',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nume', models.CharField(max_length=264, null=True)),
                ('email', models.EmailField(max_length=254, null=True)),
                ('mesaj', models.TextField(max_length=9000, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='MesajCopil',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mesaj', models.TextField(max_length=9000)),
            ],
        ),
        migrations.CreateModel(
            name='MesajServiciu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nume', models.CharField(max_length=264, null=True)),
                ('email', models.EmailField(max_length=254, null=True)),
                ('mesaj', models.TextField(max_length=9000, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='SearchBarCopil',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('search', models.CharField(max_length=264, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Serviciu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titlul', models.CharField(max_length=264, null=True)),
                ('numele_serviciului', models.CharField(max_length=264, null=True)),
                ('descriere', models.TextField(max_length=9000, null=True)),
                ('imagine', models.ImageField(blank=True, null=True, unique=True, upload_to='images/')),
                ('imagine2', models.ImageField(blank=True, null=True, unique=True, upload_to='images/')),
                ('imagine3', models.ImageField(blank=True, null=True, unique=True, upload_to='images/')),
                ('imagine4', models.ImageField(blank=True, null=True, unique=True, upload_to='images/')),
                ('imagine5', models.ImageField(blank=True, null=True, unique=True, upload_to='images/')),
                ('imagine6', models.ImageField(blank=True, null=True, unique=True, upload_to='images/')),
                ('judet', models.CharField(choices=[('Alba', 'Alba'), ('Arad', 'Arad'), ('Arges', 'Arges'), ('Bacau', 'Bacau'), ('Bihor', 'Bihor'), ('Bistrita-Nasaud', 'Bistrita-Nasaud'), ('Botosani', 'Botosani'), ('Braila', 'Braila'), ('Brasov', 'Brasov'), ('Buzau', 'Buzau'), ('Calarasi', 'Calarasi'), ('Caras-Severin', 'Caras-Severin'), ('Cluj', 'Cluj'), ('Constanta', 'Constanta'), ('Covasna', 'Covasna'), ('Dambovita', 'Dambovita'), ('Dolj', 'Dolj'), ('Galati', 'Galati'), ('Giurgiu', 'Giurgiu'), ('Gorj', 'Gorj'), ('Harghita', 'Harghita'), ('Hunedoara', 'Hunedoara'), ('Ialomita', 'Ialomita'), ('Iasi', 'Iasi'), ('Ilfov', 'Ilfov'), ('Maramures', 'Maramures'), ('Mehedinti', 'Mehedinti'), ('Mures', 'Mures'), ('Neamt', 'Neamt'), ('Olt', 'Olt'), ('Prahova', 'Prahova'), ('Salaj', 'Salaj'), ('Satu Mare', 'Satu Mare'), ('Sibiu', 'Sibiu'), ('Suceava', 'Suceava'), ('Teleorman', 'Teleorman'), ('Timis', 'Timis'), ('Tulcea', 'Tulcea'), ('Valcea', 'Valcea'), ('Vaslui', 'Vaslui'), ('Vrancea', 'Vrancea')], max_length=264)),
                ('tipul_serviciului', models.CharField(choices=[('Contabilitate', 'Contabilitate'), ('Consultanta', 'Consultanta'), ('Digital Marketing', 'Digital Marketing'), ('Grafic si Design', 'Grafic si Design'), ('Meditatii', 'Meditatii'), ('Programare si tehnologie', 'Programare si tehnologie'), ('Video si animatii', 'Video si animatii')], max_length=264)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('experienta_profesionala', models.TextField(max_length=9000, null=True)),
                ('telefon', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='AnuntAdult',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titlul', models.CharField(max_length=264, null=True)),
                ('descriere', models.TextField(max_length=9000)),
                ('numele_anuntului', models.CharField(max_length=264, null=True)),
                ('categorie_adult', models.CharField(max_length=264, null=True)),
                ('telefon', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('pret', models.CharField(default=1, max_length=264, null=True)),
                ('moneda', models.CharField(max_length=264, null=True)),
                ('imagine', models.ImageField(upload_to='images/')),
                ('imagine2', models.ImageField(null=True, upload_to='images/')),
                ('imagine3', models.ImageField(null=True, upload_to='images/')),
                ('imagine4', models.ImageField(null=True, upload_to='images/')),
                ('imagine5', models.ImageField(null=True, upload_to='images/')),
                ('imagine6', models.ImageField(null=True, upload_to='images/')),
                ('subcategorie_adult', models.CharField(max_length=264, null=True)),
                ('localizare', models.CharField(choices=[('Alba', 'Alba'), ('Arad', 'Arad'), ('Arges', 'Arges'), ('Bacau', 'Bacau'), ('Bihor', 'Bihor'), ('Bistrita-Nasaud', 'Bistrita-Nasaud'), ('Botosani', 'Botosani'), ('Braila', 'Braila'), ('Brasov', 'Brasov'), ('Buzau', 'Buzau'), ('Calarasi', 'Calarasi'), ('Caras-Severin', 'Caras-Severin'), ('Cluj', 'Cluj'), ('Constanta', 'Constanta'), ('Covasna', 'Covasna'), ('Dambovita', 'Dambovita'), ('Dolj', 'Dolj'), ('Galati', 'Galati'), ('Giurgiu', 'Giurgiu'), ('Gorj', 'Gorj'), ('Harghita', 'Harghita'), ('Hunedoara', 'Hunedoara'), ('Ialomita', 'Ialomita'), ('Iasi', 'Iasi'), ('Ilfov', 'Ilfov'), ('Maramures', 'Maramures'), ('Mehedinti', 'Mehedinti'), ('Mures', 'Mures'), ('Neamt', 'Neamt'), ('Olt', 'Olt'), ('Prahova', 'Prahova'), ('Salaj', 'Salaj'), ('Satu Mare', 'Satu Mare'), ('Sibiu', 'Sibiu'), ('Suceava', 'Suceava'), ('Teleorman', 'Teleorman'), ('Timis', 'Timis'), ('Tulcea', 'Tulcea'), ('Valcea', 'Valcea'), ('Vaslui', 'Vaslui'), ('Vrancea', 'Vrancea')], max_length=264)),
                ('capacitate_motor', models.CharField(max_length=264, null=True)),
                ('combustibil', models.CharField(max_length=264, null=True)),
                ('culoare', models.CharField(max_length=264, null=True)),
                ('cutie_de_viteze', models.CharField(max_length=264, null=True)),
                ('marca', models.CharField(max_length=264, null=True)),
                ('rulaj', models.CharField(max_length=264, null=True)),
                ('stare', models.CharField(max_length=264, null=True)),
                ('numar_de_camere', models.CharField(max_length=264, null=True)),
                ('compartimentare', models.CharField(max_length=264, null=True)),
                ('suprafata_utila', models.CharField(max_length=264, null=True)),
                ('an_de_constructie', models.CharField(max_length=264, null=True)),
                ('etaj', models.CharField(max_length=264, null=True)),
                ('teren', models.CharField(max_length=264, null=True)),
                ('marime', models.CharField(max_length=264, null=True)),
                ('tip_job', models.CharField(max_length=264, null=True)),
                ('tip_contract', models.CharField(max_length=264, null=True)),
                ('nivelul_de_studii', models.CharField(max_length=264, null=True)),
                ('nivelul_de_experienta', models.CharField(max_length=264, null=True)),
                ('mobilitatea_postului', models.CharField(max_length=264, null=True)),
                ('program_flexibil', models.CharField(max_length=264, null=True)),
                ('favorit', models.ManyToManyField(blank=True, related_name='favorit', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Adult',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nume', models.CharField(max_length=264, null=True)),
                ('emailul', models.EmailField(max_length=254, null=True)),
                ('parola', models.CharField(max_length=264, null=True)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
