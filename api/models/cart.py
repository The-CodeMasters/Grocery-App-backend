from django.db import models
from . import usertb
from . import product


class Cart(models.Model):
    quantity = models.IntegerField(default=1)
    user = models.ForeignKey(usertb.UserTable, on_delete=models.CASCADE)
    product = models.ForeignKey(product.Product, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.name}({self.user.id}) added {self.product.name}({self.product.id}) in cart'
