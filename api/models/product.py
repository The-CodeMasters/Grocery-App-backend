from django.db import models


class Product(models.Model):

    types = (
        ('kgs', 'kgs'),
        ('peices', 'peices'),
        ('litre', 'litre')
    )

    pname = models.CharField(max_length=20)
    description = models.CharField(max_length=100)
    price = models.FloatField(default=0.0)
    quantity = models.IntegerField(default=0)
    primary_category = models.CharField(max_length=20)
    secondary_category = models.CharField(max_length=20)
    brand = models.CharField(max_length=20)
    img_path = models.ImageField(upload_to='products/')
    tags = models.CharField(max_length=20)
    rating_count = models.FloatField(default=0)
    rating = models.FloatField(default=0)
    quantity_types = models.CharField(
        max_length=10, choices=types, default='kgs')
    sold = models.IntegerField(default=0)
    offer = models.FloatField(default=0.0)

    def __str__(self):
        return f'{self.id} - {self.pname}'
