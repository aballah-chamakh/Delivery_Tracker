# Generated by Django 2.0 on 2019-03-19 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DeliveryCompany', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='deliverycompany',
            name='channel_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
