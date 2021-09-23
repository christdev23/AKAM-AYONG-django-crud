# Generated by Django 3.2.7 on 2021-09-21 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('malade', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Malades',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile', models.ImageField(upload_to='profile_all')),
                ('nom', models.CharField(max_length=100)),
                ('prenom', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('maladie', models.CharField(max_length=200)),
                ('heure_D_A', models.TimeField()),
                ('heure_D_D', models.TimeField()),
                ('date_A', models.DateField()),
                ('date_d', models.DateField()),
                ('description', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='Malade',
        ),
    ]
