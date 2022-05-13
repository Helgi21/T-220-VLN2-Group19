from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

User = get_user_model()


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Condition(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Province(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Location(models.Model):
    postal_code = models.IntegerField(validators=[MinValueValidator(100), MaxValueValidator(999)])
    name = models.CharField(max_length=255)
    prov = models.ForeignKey(Province, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.postal_code) + ' ' + self.name + ' ' + str(self.prov)


class Auction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    price = models.PositiveIntegerField()
    loc = models.ForeignKey(Location, on_delete=models.CASCADE)
    cat = models.ForeignKey(Category, on_delete=models.CASCADE)
    condition = models.ForeignKey(Condition, on_delete=models.CASCADE)
    creation_time = models.DateTimeField(auto_now_add=True)
    is_finished = models.BooleanField(default=False)


class Image(models.Model):
    link = models.CharField(max_length=255)
    auction = models.ForeignKey(Auction, on_delete=models.CASCADE, related_name='images')


class Offer(models.Model):
    class OfferStatus(models.IntegerChoices):
        PEND = 1, _('Pending')
        COUNT = 2, _('Counter')
        DECL = 3, _('Declined')
        ACC = 4, _('Accepted')
        PAID = 5, _('Paid')

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    auction = models.ForeignKey(Auction, on_delete=models.CASCADE)
    price = models.PositiveIntegerField()
    status = models.IntegerField(choices=OfferStatus.choices, validators=[MinValueValidator(1), MaxValueValidator(5)])
    seller_has_reviewed = models.BooleanField(default=False)
    buyer_has_reviewed = models.BooleanField(default=False)
    # auto_now instead of auto_now_add because this should be updated whenever changed
    creation_time = models.DateTimeField(auto_now=True, null=True)

    def get_status(self):
        return self.OfferStatus(self.status).label

    # def get_highest_price(self):
    #     highest_price = self.objects.aggregate(Max('price'))['highest_price']
    #     return self.objects.filter(status=highest_price).first()
