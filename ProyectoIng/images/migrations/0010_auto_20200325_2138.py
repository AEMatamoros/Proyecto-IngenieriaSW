# Generated by Django 3.0.3 on 2020-03-26 03:38

from django.db import migrations, models
import images.models


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0009_auto_20200316_0949'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='img_route',
            field=models.ImageField(upload_to=images.models.images_directory_path, verbose_name='Ruta de la Imagen'),
        ),
    ]