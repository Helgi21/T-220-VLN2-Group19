from django.db import models

# Create your models here.
from django.utils.translation.trans_real import catalog


class User(models.Model):
    name = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    birthday = models.DateField()
    is_admin = models.BooleanField()

class Category(models.Model):
    name = models.CharField(max_length=255)

class Tag(models.Model):
    name = models.CharField(max_length=255)

class Auction(models.Model):
    UID = models.ForeignKey(user, on_delete=models.CASCADE)
    description = models.CharField(max_length=255)
    price = models.IntegerField()
    locID =
    catID = models.ForeignKey(Cetegory, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)




