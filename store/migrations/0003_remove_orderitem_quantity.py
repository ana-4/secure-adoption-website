# Generated by Django 5.1.2 on 2024-10-24 10:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_remove_product_digital_product_age_product_gender'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderitem',
            name='quantity',
        ),
    ]
