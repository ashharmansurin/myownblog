# Generated by Django 3.1.2 on 2020-10-24 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0005_post_short_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='pro_image',
            field=models.ImageField(blank=True, default='default.png', upload_to='profileimage'),
        ),
    ]