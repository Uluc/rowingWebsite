# Generated by Django 3.0.2 on 2020-05-25 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rowingWebsiteApp', '0050_auto_20200525_0827'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aboutpage',
            name='image2',
            field=models.ImageField(upload_to='template_photos'),
        ),
        migrations.AlterField(
            model_name='aboutpage',
            name='image3',
            field=models.ImageField(upload_to='template_photos'),
        ),
    ]
