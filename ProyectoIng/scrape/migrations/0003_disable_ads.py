# Generated by Django 3.0.3 on 2020-05-07 00:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scrape', '0002_auto_20200501_1908'),
    ]

    operations = [
        migrations.CreateModel(
            name='Disable_ads',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_dis', models.IntegerField(verbose_name='Desabilitar Anuncio')),
            ],
        ),
    ]
