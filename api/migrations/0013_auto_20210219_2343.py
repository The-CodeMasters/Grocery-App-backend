# Generated by Django 3.0.2 on 2021-02-19 18:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0012_auto_20210219_2338'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdminUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('admin_name', models.CharField(max_length=20)),
                ('phone', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=254)),
                ('address', models.CharField(max_length=50)),
                ('role', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='DeliveryUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('delivery_name', models.CharField(max_length=20)),
                ('phone', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=254)),
                ('address', models.CharField(max_length=50)),
            ],
        ),
        migrations.RenameField(
            model_name='product',
            old_name='name',
            new_name='pname',
        ),
        migrations.CreateModel(
            name='PromoUsed',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('used', models.IntegerField(default=0)),
                ('promo_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.PromoCode')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.UserTable')),
            ],
        ),
        migrations.CreateModel(
            name='DeliveryHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_time', models.DateTimeField(auto_now_add=True)),
                ('delivery_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.DeliveryUser')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Order')),
            ],
        ),
    ]