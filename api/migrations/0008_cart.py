# Generated by Django 3.0.2 on 2021-02-18 18:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_auto_20210218_2253'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=1)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.User_table')),
            ],
        ),
    ]
