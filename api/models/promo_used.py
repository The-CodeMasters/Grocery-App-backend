from django.db import models
from . import usertb
from . import promo_code


class PromoUsed(models.Model):
    user = models.ForeignKey(usertb.UserTable, on_delete=models.CASCADE)
    promo_code = models.ForeignKey(
        promo_code.PromoCode, on_delete=models.CASCADE)
    used = models.IntegerField(default=0)

    def __str__(self):
        return f'{user.name}({user.id}) used promo {self.promo_code.promo_name} {self.used} times '
