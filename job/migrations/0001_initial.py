# Generated by Django 3.2 on 2021-04-25 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AnnouncedJobs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active_job', models.BooleanField(default=True)),
                ('position_title', models.CharField(max_length=256)),
                ('experienced', models.CharField(max_length=256)),
                ('qualification', models.CharField(max_length=256)),
                ('knowledge', models.CharField(max_length=256)),
                ('job_responsibility', models.CharField(max_length=256)),
                ('skill_set', models.CharField(max_length=256)),
                ('description', models.TextField()),
                ('Degree', models.SmallIntegerField(choices=[(1, 'MATRIC or more'), (2, 'FSC or more'), (3, 'BS or more'), (4, 'MS or more')])),
                ('experience', models.IntegerField(choices=[(1, 'ONE or more'), (2, 'TWO or more'), (3, 'THREE or more'), (4, 'FOUR or more')])),
            ],
            options={
                'verbose_name': 'Jobs',
            },
        ),
    ]