from django.db import models


class PrimaryCategory(models.Model):
    prim_name = models.CharField(max_length=20)
