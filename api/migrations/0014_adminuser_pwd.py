# Generated by Django 3.0.2 on 2021-02-21 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0013_auto_20210219_2343'),
    ]

    operations = [
        migrations.AddField(
            model_name='adminuser',
            name='pwd',
            field=models.CharField(default='', max_length=20),
            preserve_default=False,
        ),
    ]
