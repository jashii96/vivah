# Generated by Django 2.1 on 2021-12-28 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('matrimony', '0002_auto_20211228_0950'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='phone',
            field=models.CharField(max_length=15),
        ),
    ]
