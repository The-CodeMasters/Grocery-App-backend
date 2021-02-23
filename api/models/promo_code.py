from django.db import models


class PromoCode(models.Model):
    promo_name = models.CharField(max_length=10)
    discount = models.IntegerField(default=0)
    status = models.CharField(max_length=20)
    max_usage = models.IntegerField()

    def __str__(self):
        return f'{self.promo_name}({self.id}) status - {self.status}'
