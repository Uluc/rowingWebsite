# Generated by Django 3.0.2 on 2020-05-18 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rowingWebsiteApp', '0046_auto_20200518_0727'),
    ]

    operations = [
        migrations.CreateModel(
            name='HomePage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32)),
                ('text', models.TextField(help_text='This will be the text that gets displayed')),
                ('image', models.ImageField(upload_to='template_photos')),
            ],
        ),
        migrations.CreateModel(
            name='RecruitmentPage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32)),
                ('text', models.TextField(help_text='This will be the text that gets displayed')),
                ('questionaire_link', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='SponsorPage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32)),
                ('text', models.TextField(help_text='This will be the text that gets displayed')),
                ('sponsorship_coordinator_name', models.CharField(max_length=64)),
                ('sponsorship_coordinator_email', models.EmailField(help_text='Refer to LSU email', max_length=254)),
                ('image', models.ImageField(upload_to='template_photos')),
            ],
        ),
    ]
