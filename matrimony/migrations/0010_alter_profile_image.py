# Generated by Django 4.0 on 2022-01-19 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('matrimony', '0009_alter_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(upload_to='profile_pics'),
        ),
    ]
