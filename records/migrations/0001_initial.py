# Generated by Django 2.1.1 on 2020-06-21 17:36

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('listings', '0005_listing_parking'),
    ]

    operations = [
        migrations.CreateModel(
            name='Expense',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(default=datetime.datetime.now)),
                ('category', models.CharField(max_length=200)),
                ('vendor', models.CharField(max_length=200)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=11)),
                ('note', models.CharField(max_length=200)),
                ('unit', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='listings.Listing')),
            ],
        ),
        migrations.CreateModel(
            name='Revenue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(default=datetime.datetime.now)),
                ('category', models.CharField(max_length=200)),
                ('guest', models.CharField(max_length=200)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=11)),
                ('note', models.CharField(max_length=200)),
                ('unit', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='listings.Listing')),
            ],
        ),
    ]
