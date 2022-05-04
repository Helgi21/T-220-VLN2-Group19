# Generated by Django 4.0.4 on 2022-05-04 02:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0009_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='auction',
        ),
        migrations.RemoveField(
            model_name='location',
            name='prov',
        ),
        migrations.RemoveField(
            model_name='offer',
            name='auction',
        ),
        migrations.RemoveField(
            model_name='offer',
            name='user',
        ),
        migrations.DeleteModel(
            name='Auction',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='Image',
        ),
        migrations.DeleteModel(
            name='Location',
        ),
        migrations.DeleteModel(
            name='Offer',
        ),
        migrations.DeleteModel(
            name='Province',
        ),
        migrations.DeleteModel(
            name='Tag',
        ),
    ]
