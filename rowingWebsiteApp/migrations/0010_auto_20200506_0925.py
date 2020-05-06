# Generated by Django 3.0.2 on 2020-05-06 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rowingWebsiteApp', '0009_rowers_year'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rowers',
            name='year',
            field=models.CharField(choices=[('Freshmen', 'FR'), ('Sophmore', 'SO'), ('Junior', 'JR'), ('Senior', 'SR')], max_length=64),
        ),
    ]
