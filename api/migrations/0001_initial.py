# Generated by Django 3.0.2 on 2021-02-16 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='userTable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('userid', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=10)),
                ('coordinates', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('address', models.CharField(max_length=50)),
                ('role', models.CharField(max_length=10)),
            ],
        ),
    ]
