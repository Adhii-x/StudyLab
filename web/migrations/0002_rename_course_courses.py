# Generated by Django 4.2.5 on 2023-09-26 01:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='course',
            new_name='courses',
        ),
    ]