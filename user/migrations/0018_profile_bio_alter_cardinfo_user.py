# Generated by Django 4.0.4 on 2022-05-09 12:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('user', '0017_alter_cardinfo_card_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='bio',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='cardinfo',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cards', to=settings.AUTH_USER_MODEL),
        ),
    ]
