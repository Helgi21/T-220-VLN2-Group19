# Generated by Django 4.0.4 on 2022-05-06 13:38

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auction', '0005_alter_auction_price_alter_offer_price_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='postal_code',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(100), django.core.validators.MaxValueValidator(999)]),
        ),
        migrations.AlterField(
            model_name='offer',
            name='status',
            field=models.IntegerField(choices=[(1, 'Pending'), (2, 'Counter'), (3, 'Declined'), (4, 'Accepted'), (5, 'Paid')], validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)]),
        ),
    ]
