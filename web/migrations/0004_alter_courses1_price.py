# Generated by Django 4.2.5 on 2023-10-02 00:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_courses1'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courses1',
            name='price',
            field=models.IntegerField(),
        ),
    ]
