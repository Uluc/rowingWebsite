# Generated by Django 3.0.2 on 2020-05-16 01:16

from django.db import migrations, models
import sortedm2m.fields


class Migration(migrations.Migration):

    dependencies = [
        ('rowingWebsiteApp', '0028_auto_20200516_0038'),
    ]

    operations = [
        migrations.AddField(
            model_name='gallery',
            name='date',
            field=models.CharField(default='Gallery', max_length=64),
        ),
        migrations.AlterField(
            model_name='gallery',
            name='photos',
            field=sortedm2m.fields.SortedManyToManyField(help_text=None, to='rowingWebsiteApp.Picture'),
        ),
    ]
