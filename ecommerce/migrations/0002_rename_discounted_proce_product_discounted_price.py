# Generated by Django 4.2.3 on 2023-07-15 03:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='discounted_proce',
            new_name='discounted_price',
        ),
    ]
