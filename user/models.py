from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()
from django.utils.translation import gettext_lazy as _
from auction import models as auction_models

# Create your models here.
""" REPLACED BY AUTH_USER BUILT INTO DJANGO
class User(models.Model):
    name = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    birthday = models.DateField()
    is_admin = models.BooleanField()

    def __str__(self):
        return self.name
"""


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    profile_picture = models.CharField(max_length=999, null=True)
    birthday = models.DateField(null=True)
    bio = models.CharField(max_length=255, null=True)
    # 0-10, 0 = 0 star, 5 = 2.5 star, 10 = 5 star
    rating = models.PositiveIntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(10)])


class Report(models.Model):
    class ReportsTypes(models.IntegerChoices):
        USER = 1, _("user")
        BUG = 2, _("bug")
    reported_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reports_against', default=None,
                                      null=True)
    reporter_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reports_made')
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    report_type = models.PositiveIntegerField(choices=ReportsTypes.choices,
                                              validators=[MinValueValidator(1), MaxValueValidator(2)])


class Review(models.Model):
    class ReviewType(models.IntegerChoices):
        SALE = 1, _('sale')
        PURCHASE = 2, _('purchase')

    reviewed_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews_against')
    reviewer_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews_made')
    description = models.CharField(max_length=255)
    rating = models.PositiveIntegerField(validators=[MinValueValidator(0), MaxValueValidator(10)])
    type = models.PositiveIntegerField(choices=ReviewType.choices,
                                       validators=[MinValueValidator(1), MaxValueValidator(2)])
    offer = models.ForeignKey(auction_models.Offer, on_delete=models.CASCADE, related_name='offer_reviews')


class CardInfo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="cards")
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    card_number = models.BigIntegerField(validators=[MinValueValidator(1000000000000000),
                                                     MaxValueValidator(9999999999999999)])
    cvc = models.SmallIntegerField(validators=[MinValueValidator(100), MaxValueValidator(999)])
    expires = models.DateField()
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    region = models.CharField(max_length=255)
    zip = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
