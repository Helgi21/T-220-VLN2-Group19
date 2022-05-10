# Generated by Django 4.0.4 on 2022-05-09 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auction', '0006_alter_location_postal_code_alter_offer_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Condition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.RemoveField(
            model_name='auction',
            name='tag',
        ),
        migrations.DeleteModel(
            name='Tag',
        ),
    ]
