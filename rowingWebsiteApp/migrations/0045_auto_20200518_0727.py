# Generated by Django 3.0.2 on 2020-05-18 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rowingWebsiteApp', '0044_auto_20200518_0721'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='sponsor',
            options={'ordering': ['last_name']},
        ),
        migrations.RemoveField(
            model_name='sponsor',
            name='name',
        ),
        migrations.AddField(
            model_name='sponsor',
            name='first_name',
            field=models.CharField(default=' ', max_length=64),
        ),
        migrations.AddField(
            model_name='sponsor',
            name='last_name',
            field=models.CharField(default=' ', max_length=64),
        ),
    ]
