# Generated by Django 3.0.2 on 2020-05-17 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rowingWebsiteApp', '0036_auto_20200517_0632'),
    ]

    operations = [
        migrations.AlterField(
            model_name='race',
            name='date',
            field=models.CharField(max_length=64),
        ),
    ]
