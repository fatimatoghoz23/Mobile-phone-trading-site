# Generated by Django 4.2 on 2023-04-15 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0017_remove_product_index'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='c',
            field=models.CharField(choices=[('i', 'i'), ('p', 'p')], max_length=100, null=True),
        ),
    ]
