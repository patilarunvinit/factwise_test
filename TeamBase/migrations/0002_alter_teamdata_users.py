# Generated by Django 4.2.7 on 2023-11-03 22:06

from django.db import migrations, models
import django_mysql.models


class Migration(migrations.Migration):

    dependencies = [
        ('TeamBase', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teamdata',
            name='users',
            field=django_mysql.models.ListCharField(models.IntegerField(), max_length=66, size=6),
        ),
    ]