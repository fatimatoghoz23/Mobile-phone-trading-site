# Generated by Django 4.2 on 2023-04-14 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='ram',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
