# Generated by Django 4.2.7 on 2023-11-03 22:12

from django.db import migrations, models
import django_mysql.models


class Migration(migrations.Migration):

    dependencies = [
        ('TeamBase', '0003_alter_teamdata_users'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teamdata',
            name='users',
            field=django_mysql.models.ListCharField(models.IntegerField(), max_length=2, size=None),
        ),
    ]
