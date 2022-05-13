# Generated by Django 4.0.4 on 2022-05-12 20:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auction', '0009_offer_buyer_has_reviewed_offer_seller_has_reviewed'),
        ('user', '0019_alter_profile_birthday_alter_profile_profile_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='offer',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='offer_reviews', to='auction.offer'),
            preserve_default=False,
        ),
    ]