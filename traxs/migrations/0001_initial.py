# Generated by Django 4.2 on 2023-04-04 05:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Trax',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('workout', models.CharField(max_length=100)),
                ('meal', models.CharField(max_length=100)),
                ('weight', models.CharField(max_length=100)),
                ('notes', models.CharField(max_length=100)),
            ],
        ),
    ]
