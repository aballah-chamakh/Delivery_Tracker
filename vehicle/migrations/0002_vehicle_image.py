# Generated by Django 2.0 on 2019-03-10 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicle', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehicle',
            name='image',
            field=models.ImageField(default='vehicle_img.jpg', upload_to=''),
        ),
    ]
