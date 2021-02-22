from django.db import models
from . import product
from . import usertb


class FavouriteProduct(models.Model):
    product = models.ForeignKey(product.Product, on_delete=models.CASCADE)
    user = models.ForeignKey(usertb.UserTable, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.name}({self.user.id}) liked {self.product.name}({self.product.id}) '
