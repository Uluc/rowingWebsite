# Generated by Django 3.0.2 on 2020-05-17 04:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rowingWebsiteApp', '0034_auto_20200517_0346'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='race',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
