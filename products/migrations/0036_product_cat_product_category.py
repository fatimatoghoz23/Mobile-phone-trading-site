# Generated by Django 4.2 on 2023-04-16 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0035_remove_product_cat_remove_product_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='cat',
            field=models.CharField(choices=[('i', 'i'), ('p', 'p')], max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('photo', 'photo'), ('computer', 'computer')], max_length=100, null=True),
        ),
    ]
