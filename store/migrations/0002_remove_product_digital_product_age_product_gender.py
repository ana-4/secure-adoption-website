# Generated by Django 5.1.2 on 2024-10-24 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='digital',
        ),
        migrations.AddField(
            model_name='product',
            name='age',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='product',
            name='gender',
            field=models.CharField(default='Not Specified', max_length=200),
        ),
    ]
