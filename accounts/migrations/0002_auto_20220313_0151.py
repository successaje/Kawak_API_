# Generated by Django 3.0.14 on 2022-03-13 00:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='first_name',
            field=models.CharField(default=True, max_length=255),
        ),
        migrations.AddField(
            model_name='user',
            name='last_name',
            field=models.CharField(default=True, max_length=255),
        ),
    ]
