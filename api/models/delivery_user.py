from django.db import models


class DeliveryUser(models.Model):
    delivery_name = models.CharField(max_length=20)
    phone = models.CharField(max_length=10)
    email = models.EmailField()
    pwd = models.CharField(max_length=50)

    address = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.id} - {self.delivery_name}'
