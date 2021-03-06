# Generated by Django 3.0.2 on 2020-06-02 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rowingWebsiteApp', '0059_auto_20200601_1753'),
    ]

    operations = [
        migrations.AddField(
            model_name='recruitmentpage',
            name='image',
            field=models.ImageField(default='none', help_text='This will be the image that gets displayed under the text', upload_to='recruitmentPagePictures'),
        ),
        migrations.AlterField(
            model_name='pagebanners',
            name='about_page_title',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='pagebanners',
            name='recruitment_page_title',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='pagebanners',
            name='schedule_page_title',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='pagebanners',
            name='sponsor_page_title',
            field=models.CharField(max_length=50),
        ),
    ]
