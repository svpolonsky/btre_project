# Generated by Django 2.1.1 on 2020-07-01 15:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('owners', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='owner',
            name='user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]
