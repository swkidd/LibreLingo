# Generated by Django 3.0.1 on 2020-01-02 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0002_auto_20200102_1935'),
    ]

    operations = [
        migrations.CreateModel(
            name='Module',
            fields=[
                ('id',
                 models.AutoField(
                     auto_created=True,
                     primary_key=True,
                     serialize=False,
                     verbose_name='ID')),
                ('name',
                 models.TextField(
                     verbose_name='Language name')),
            ],
            options={
                'verbose_name': 'Module',
            },
        ),
    ]
