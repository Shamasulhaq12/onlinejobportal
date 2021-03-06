# Generated by Django 3.2 on 2021-04-23 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applications', '0004_auto_20210423_1420'),
    ]

    operations = [
        migrations.AlterField(
            model_name='qualifiedcv',
            name='date_of_birth',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='qualifiedcv',
            name='degree_date_1',
            field=models.CharField(default='', max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='qualifiedcv',
            name='degree_date_2',
            field=models.CharField(default='', max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='qualifiedcv',
            name='degree_date_3',
            field=models.CharField(default='', max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='unqualifiedcv',
            name='date_of_birth',
            field=models.DateField(),
        ),
    ]
