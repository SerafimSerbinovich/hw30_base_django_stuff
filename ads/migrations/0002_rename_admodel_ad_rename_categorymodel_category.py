# Generated by Django 4.1.5 on 2023-01-30 13:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
        ('ads', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='AdModel',
            new_name='Ad',
        ),
        migrations.RenameModel(
            old_name='CategoryModel',
            new_name='Category',
        ),
    ]
