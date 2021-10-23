# Generated by Django 3.2.8 on 2021-10-23 08:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('advisor2', '0006_auto_20211023_1355'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='adid',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='uid',
        ),
        migrations.AddField(
            model_name='booking',
            name='advisor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='advisors', to='advisor2.advisor'),
        ),
        migrations.AddField(
            model_name='booking',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='users', to=settings.AUTH_USER_MODEL),
        ),
    ]
