# Generated by Django 3.0.2 on 2021-02-19 08:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_favouriteproduct'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User_table',
            new_name='UserTable',
        ),
    ]