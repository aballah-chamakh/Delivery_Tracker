# Generated by Django 2.0 on 2019-03-19 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('driver', '0004_auto_20190317_1623'),
    ]

    operations = [
        migrations.AddField(
            model_name='driver',
            name='channel_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
