from django.db import models


# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    birthday = models.DateField()
    is_admin = models.BooleanField()


class Category(models.Model):
    name = models.CharField(max_length=255)


class Tag(models.Model):
    name = models.CharField(max_length=255)


class Province(models.Model):
    name = models.CharField(max_length=255)


class Location(models.Model):
    postal_code = models.IntegerField()
    name = models.CharField(max_length=255)
    provID = models.ForeignKey(Province, on_delete=models.CASCADE)


class Auction(models.Model):
    UID = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=255)
    price = models.IntegerField()
    locID = models.ForeignKey(Location, on_delete=models.CASCADE)
    catID = models.ForeignKey(Category, on_delete=models.CASCADE)
    tag = models.ManyToManyField(Tag)


class Report(models.Model):
    class ReportsTypes(models.IntegerChoices):
        USER = 1, "user"
        BUG = 2, "bug"
    UID = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reports_against')
    RUID = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reports_made')
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    report_type = models.CharField(max_length=1, choices=ReportsTypes.choices)


class Review(models.Model):
    class ReviewType(models.IntegerChoices):
        SALE = 1, 'sale'
        PURCHASE = 2, 'purchase'

    reviewedID = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews_against')
    reviewerID = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews_made')
    description = models.CharField(max_length=255)
    rating = models.IntegerField()  # TODO: debate integer 0-10 or float 0.0-5.0
    type = models.CharField(max_length=1, choices=ReviewType.choices)


class Offer(models.Model):
    class OfferStatus(models.IntegerChoices):
        PEND = 1, 'pending'
        COUNT = 2, 'counter'
        DECL = 3, 'declined'
        ACC = 4, 'accepted'
        PAID = 5, 'paid'

    UID = models.ForeignKey(User, on_delete=models.CASCADE)
    auctionID = models.ForeignKey(Auction, on_delete=models.CASCADE)
    price = models.IntegerField()
    status = models.CharField(max_length=1, choices=OfferStatus.choices)


class CardInfo(models.Model):
    UID = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    card_number = models.IntegerField()
    cvc = models.IntegerField()
    expires = models.DateField()
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    region = models.CharField(max_length=255)
    zip = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
