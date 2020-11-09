# Generated by Django 3.1.2 on 2020-10-25 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0010_auto_20201025_1940'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='bio',
            field=models.CharField(blank=True, max_length=250),
        ),
        migrations.AlterField(
            model_name='profile',
            name='education',
            field=models.CharField(blank=True, choices=[('M.C.A', 'M.C.A'), ('B.C.A', 'B.C.A'), ('B.A', 'B.A'), ('M.A', 'M.A'), ('P.G', 'P.G'), ('HIGH SCHOOL', 'HIGH SCOOL'), ('SECONDARY', 'SECONDARY')], max_length=50),
        ),
        migrations.AlterField(
            model_name='profile',
            name='works',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]