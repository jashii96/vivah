# Generated by Django 4.0 on 2022-01-25 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('matrimony', '0011_familydetails_married_brother_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='familydetails',
            name='brothers',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='familydetails',
            name='family_status',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='familydetails',
            name='family_type',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='familydetails',
            name='family_value',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='familydetails',
            name='father_occupation',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='familydetails',
            name='married_brother',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='familydetails',
            name='married_sister',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='familydetails',
            name='mother_occupation',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='familydetails',
            name='sisters',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='personalinfo',
            name='caste',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='personalinfo',
            name='child_status',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='personalinfo',
            name='city',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='personalinfo',
            name='country',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='personalinfo',
            name='dob',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='personalinfo',
            name='gender',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='personalinfo',
            name='marital_status',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='personalinfo',
            name='mobile',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='personalinfo',
            name='mother_tongue',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='personalinfo',
            name='no_ofchild',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='personalinfo',
            name='religion',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='personalinfo',
            name='state',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='profile_pics'),
        ),
    ]
