from django.db import models
from . import order
from . import product


class OrderItem(models.Model):
    order = models.ForeignKey(order.Order, on_delete=models.CASCADE)
    product = models.ForeignKey(product.Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return self.order.id
