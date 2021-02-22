from django.db import models
from . import usertb
from . import promo_code


class Order(models.Model):
    user = models.ForeignKey(usertb.UserTable, on_delete=models.CASCADE)
    status = models.CharField(max_length=20)
    grand_total = models.FloatField(default=0.0)
    date_time = models.DateTimeField(auto_now_add=True)
    promocode = models.ForeignKey(
        promo_code.PromoCode, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f'{self.user.name}({self.user.id}) has made an Order at {self.date_time}'
