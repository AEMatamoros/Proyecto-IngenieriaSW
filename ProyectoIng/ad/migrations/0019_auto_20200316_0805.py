# Generated by Django 3.0.3 on 2020-03-16 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ad', '0018_ad_ad_images'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ad',
            name='ad_images',
        ),
        migrations.AddField(
            model_name='ad',
            name='ad_images',
            field=models.ImageField(blank='False', upload_to='Ad_Image'),
        ),
    ]