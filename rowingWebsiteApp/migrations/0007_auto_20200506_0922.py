# Generated by Django 3.0.2 on 2020-05-06 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rowingWebsiteApp', '0006_auto_20200506_0922'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rowers',
            name='crew',
            field=models.CharField(choices=[('Mens', 'Mens'), ('Womens', 'Womens')], max_length=64),
        ),
    ]