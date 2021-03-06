# Generated by Django 4.0.4 on 2022-05-05 10:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auction', '0002_alter_auction_user_alter_image_auction_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('user', '0010_remove_image_auction_remove_location_prov_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cardinfo',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='report',
            name='reported_user',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reports_against', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='report',
            name='reporter_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reports_made', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='review',
            name='reviewed_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews_against', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='review',
            name='reviewer_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews_made', to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
