# Generated by Django 4.0.4 on 2022-05-05 15:58

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('auction', '0002_alter_auction_user_alter_image_auction_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='auction',
            name='creation_time',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
