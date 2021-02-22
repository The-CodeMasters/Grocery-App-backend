from django.db import models
from . import primary_cat


class SecondaryCategory(models.Model):
    primary_cat = models.ForeignKey(
        primary_cat.PrimaryCategory, on_delete=models.CASCADE)
    sec_name = models.CharField(max_length=20)
