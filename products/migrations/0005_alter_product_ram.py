# Generated by Django 4.2 on 2023-04-14 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_product_ram'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='ram',
            field=models.IntegerField(),
        ),
    ]