# Generated by Django 4.1.7 on 2023-03-21 23:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0005_band_like_new'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='band',
            name='like_new',
        ),
    ]