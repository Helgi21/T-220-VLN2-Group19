from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()

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


class Report(models.Model):
    class ReportsTypes(models.IntegerChoices):
        USER = 1, "user"
        BUG = 2, "bug"
    reported_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reports_against', default=None,
                                      null=True)
    reporter_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reports_made')
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    report_type = models.CharField(max_length=1, choices=ReportsTypes.choices)


class Review(models.Model):
    class ReviewType(models.IntegerChoices):
        SALE = 1, 'sale'
        PURCHASE = 2, 'purchase'

    reviewed_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews_against')
    reviewer_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews_made')
    description = models.CharField(max_length=255)
    rating = models.IntegerField()  # TODO: debate integer 0-10 or float 0.0-5.0
    type = models.CharField(max_length=1, choices=ReviewType.choices)


class CardInfo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    card_number = models.BigIntegerField()
    cvc = models.SmallIntegerField()
    expires = models.DateField()
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    region = models.CharField(max_length=255)
    zip = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
