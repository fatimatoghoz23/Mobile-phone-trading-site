# Generated by Django 4.2 on 2023-04-15 20:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0022_remove_product_ra'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='cat',
            field=models.CharField(max_length=190, null=True),
        ),
    ]
