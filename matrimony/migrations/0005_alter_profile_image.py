# Generated by Django 4.0 on 2022-01-18 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('matrimony', '0004_qualification_physicalattribute_photoalbum_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='sample.jpg', upload_to='profile_pics'),
        ),
    ]