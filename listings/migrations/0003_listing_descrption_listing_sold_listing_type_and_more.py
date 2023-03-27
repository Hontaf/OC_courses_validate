# Generated by Django 4.1.7 on 2023-03-21 20:22

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0002_band_active_band_biography_band_genre_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='descrption',
            field=models.CharField(default='', max_length=1000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='listing',
            name='sold',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='listing',
            name='type',
            field=models.CharField(choices=[('Re', 'Records'), ('Cl', 'Clothing'), ('Po', 'Posters'), ('Mi', 'Miscellaneous')], default='Re', max_length=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='listing',
            name='year',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(1980), django.core.validators.MaxValueValidator(2023)]),
        ),
    ]