# Generated by Django 3.1.2 on 2020-10-30 15:24

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0016_auto_20201030_2052'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photogallary',
            name='upload_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
