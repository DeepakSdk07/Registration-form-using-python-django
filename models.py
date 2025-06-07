from django.db import models

class Datas(models.Model):
    name = models.CharField(max_length=20, default="")
    age = models.IntegerField(default=0)
    address = models.CharField(max_length=50, default="")
    contact = models.BigIntegerField(default=0)
    mail = models.EmailField(max_length=50, default="")

    def __str__(self):
        return self.name
