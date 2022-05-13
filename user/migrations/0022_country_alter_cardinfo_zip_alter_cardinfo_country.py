# Generated by Django 4.0.4 on 2022-05-13 12:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0021_notification'),
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=2)),
                ('name', models.CharField(max_length=150)),
            ],
        ),
        migrations.AlterField(
            model_name='cardinfo',
            name='zip',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='cardinfo',
            name='country',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cards', to='user.country'),
        ),
    ]
