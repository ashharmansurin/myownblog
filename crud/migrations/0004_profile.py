# Generated by Django 3.1.2 on 2020-10-24 14:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('crud', '0003_auto_20201024_1817'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pro_image', models.ImageField(blank=True, upload_to='profileimage')),
                ('bio', models.CharField(max_length=250)),
                ('works', models.CharField(max_length=100)),
                ('cover', models.ImageField(blank=True, upload_to='coverimage')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]