# Generated by Django 2.1.1 on 2020-06-13 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0002_contactowner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactowner',
            name='m2',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='contactowner',
            name='rooms',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]
