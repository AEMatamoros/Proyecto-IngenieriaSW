# Generated by Django 3.0.3 on 2020-03-15 22:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ad', '0016_auto_20200315_1615'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ad',
            old_name='iduser',
            new_name='id_user',
        ),
    ]