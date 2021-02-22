from django.db import models


class AdminUser(models.Model):
    admin_name = models.CharField(max_length=20)
    phone = models.CharField(max_length=10)
    email = models.EmailField()
    adm_pwd = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    role = models.CharField(max_length=10)

    def __str__(self):
        return f'{self.id} - {self.admin_name}'
