# Generated by Django 3.0.2 on 2020-05-15 03:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rowingWebsiteApp', '0021_gallery'),
    ]

    operations = [
        migrations.AddField(
            model_name='gallery',
            name='description',
            field=models.CharField(default='Picture', max_length=64),
        ),
    ]
