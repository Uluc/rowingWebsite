# Generated by Django 3.0.2 on 2020-05-13 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rowingWebsiteApp', '0019_auto_20200512_0819'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sponsors',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
    ]
