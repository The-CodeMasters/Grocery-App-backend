# Generated by Django 3.0.2 on 2021-02-18 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_product_quantity_types'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='quantity',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.FloatField(default=0.0),
        ),
    ]
