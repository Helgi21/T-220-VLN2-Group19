# Generated by Django 4.0.4 on 2022-05-04 00:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_rename_catid_auction_cat_rename_locid_auction_loc_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='report',
            old_name='user',
            new_name='reported_user',
        ),
    ]