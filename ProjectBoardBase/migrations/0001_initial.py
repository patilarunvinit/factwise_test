# Generated by Django 4.2.7 on 2023-11-04 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BoardData',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=64, unique=True)),
                ('description', models.CharField(max_length=128)),
                ('creation_time', models.DateField(null=True)),
                ('status', models.CharField(max_length=15)),
                ('end_time', models.DateField(null=True)),
            ],
        ),
    ]
