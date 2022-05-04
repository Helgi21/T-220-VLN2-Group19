from django.db import models
from user import models as user


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Province(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Location(models.Model):
    postal_code = models.IntegerField()
    name = models.CharField(max_length=255)
    prov = models.ForeignKey(Province, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.postal_code) + ' ' + self.name + ' ' + str(self.prov)


class Auction(models.Model):
    user = models.ForeignKey(user.User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    price = models.IntegerField()
    loc = models.ForeignKey(Location, on_delete=models.CASCADE)
    cat = models.ForeignKey(Category, on_delete=models.CASCADE)
    tag = models.ManyToManyField(Tag)


class Image(models.Model):
    link = models.CharField(max_length=255)
    auction = models.ForeignKey(Auction, on_delete=models.CASCADE, related_name='images')


class Offer(models.Model):
    class OfferStatus(models.IntegerChoices):
        PEND = 1, 'pending'
        COUNT = 2, 'counter'
        DECL = 3, 'declined'
        ACC = 4, 'accepted'
        PAID = 5, 'paid'

    user = models.ForeignKey(user.User, on_delete=models.CASCADE)
    auction = models.ForeignKey(Auction, on_delete=models.CASCADE)
    price = models.IntegerField()
    status = models.CharField(max_length=1, choices=OfferStatus.choices)

