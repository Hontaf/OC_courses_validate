# Generated by Django 4.1.7 on 2023-03-21 22:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0003_listing_descrption_listing_sold_listing_type_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='band',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='listings.band'),
        ),
    ]
