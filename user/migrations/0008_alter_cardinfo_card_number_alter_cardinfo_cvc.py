# Generated by Django 4.0.4 on 2022-05-04 01:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0007_alter_report_reported_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cardinfo',
            name='card_number',
            field=models.BigIntegerField(),
        ),
        migrations.AlterField(
            model_name='cardinfo',
            name='cvc',
            field=models.SmallIntegerField(),
        ),
    ]
