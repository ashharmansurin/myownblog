# Generated by Django 3.1.2 on 2020-11-03 10:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0017_auto_20201030_2054'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='photogallary',
            name='user',
        ),
        migrations.AddField(
            model_name='profile',
            name='photo_gallary',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='crud.photogallary'),
        ),
    ]