# Generated by Django 4.2.7 on 2023-11-03 23:32

from django.db import migrations, models
import django_mysql.models


class Migration(migrations.Migration):

    dependencies = [
        ('TeamBase', '0009_alter_teamdata_users'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teamdata',
            name='users',
            field=django_mysql.models.ListCharField(models.CharField(max_length=10), max_length=22, size=2),
        ),
    ]
