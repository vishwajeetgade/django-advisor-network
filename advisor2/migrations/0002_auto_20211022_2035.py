# Generated by Django 3.2.8 on 2021-10-22 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advisor2', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advisor',
            name='name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='advisor',
            name='photo',
            field=models.URLField(),
        ),
    ]
