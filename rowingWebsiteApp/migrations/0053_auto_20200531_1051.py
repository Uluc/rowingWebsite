# Generated by Django 3.0.2 on 2020-05-31 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rowingWebsiteApp', '0052_auto_20200528_1228'),
    ]

    operations = [
        migrations.CreateModel(
            name='PageBanners',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recruitment_banner', models.ImageField(upload_to='banners')),
                ('about_banner', models.ImageField(upload_to='banners')),
                ('schedule_banner', models.ImageField(upload_to='banners')),
                ('sponsor_banner', models.ImageField(upload_to='banners')),
            ],
        ),
        migrations.RemoveField(
            model_name='aboutpage',
            name='image3',
        ),
    ]