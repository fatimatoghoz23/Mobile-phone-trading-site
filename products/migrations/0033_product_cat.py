# Generated by Django 4.2 on 2023-04-15 22:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0032_remove_product_cat'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='cat',
            field=models.CharField(choices=[('photo', 'photo'), ('computer', 'computer')], max_length=100, null=True),
        ),
    ]
