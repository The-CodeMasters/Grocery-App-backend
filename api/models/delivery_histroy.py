from django.db import models
from . import order
from . import delivery_user


class DeliveryHistory(models.Model):
    delivery_name = models.ForeignKey(
        delivery_user.DeliveryUser, on_delete=models.CASCADE)
    order = models.ForeignKey(order.Order, on_delete=models.CASCADE)
    date_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'({self.id})'
