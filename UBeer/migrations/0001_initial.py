# Generated by Django 2.1.7 on 2019-04-02 21:04

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Establishments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latitude', models.IntegerField()),
                ('longitude', models.IntegerField()),
                ('address', models.CharField(max_length=128)),
                ('zip_code', models.CharField(max_length=5)),
                ('city', models.CharField(max_length=25)),
                ('state', models.CharField(max_length=2)),
                ('minimum_tab', models.FloatField()),
                ('user', models.ForeignKey(on_delete=None, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Riders',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.ForeignKey(on_delete=None, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Transactions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total', models.FloatField()),
                ('date', models.DateTimeField()),
                ('user', models.ForeignKey(on_delete=None, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Trips',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tab', models.FloatField()),
                ('status', models.CharField(choices=[('R', 'Reserved'), ('A', 'Arrived'), ('C', 'Complete')], max_length=4)),
                ('establishment', models.ForeignKey(on_delete=None, to='UBeer.Establishments')),
                ('rider', models.ForeignKey(on_delete=None, to='UBeer.Riders')),
            ],
        ),
    ]
