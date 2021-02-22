from django.db import models

# Create your models here.


class UserTable(models.Model):
    name = models.CharField(max_length=20)
    uid = models.CharField(max_length=50)
    phone = models.CharField(max_length=10)
    coordinates = models.CharField(max_length=50)
    email = models.EmailField()
    address = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.id} - {self.name}'
