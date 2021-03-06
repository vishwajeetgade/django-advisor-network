# Generated by Django 3.2.8 on 2021-10-22 18:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('advisor2', '0002_auto_20211022_2035'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('booking_time', models.DateField()),
            ],
        ),
        migrations.AddField(
            model_name='advisor',
            name='user_id',
            field=models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='advisor',
            name='booking_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='advisor2.booking'),
        ),
    ]
