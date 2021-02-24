from django.db import models

# Create your models here.


class UserTable(models.Model):
    name = models.CharField(max_length=20)
    uid = models.CharField(max_length=50)
    phone = models.CharField(max_length=10)
    email = models.EmailField()
    addressString = models.CharField(max_length=50)
    addressCoordinate = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.id} - {self.name}'
