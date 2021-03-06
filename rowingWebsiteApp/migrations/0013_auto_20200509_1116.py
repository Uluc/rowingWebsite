# Generated by Django 3.0.2 on 2020-05-09 11:16

from django.db import migrations, models
import image_cropping.fields


class Migration(migrations.Migration):

    dependencies = [
        ('rowingWebsiteApp', '0012_auto_20200507_0748'),
    ]

    operations = [
        migrations.AddField(
            model_name='rower',
            name='cropping',
            field=image_cropping.fields.ImageRatioField('image', '430x360', adapt_rotation=False, allow_fullsize=False, free_crop=False, help_text=None, hide_image_field=False, size_warning=False, verbose_name='cropping'),
        ),
        migrations.AlterField(
            model_name='rower',
            name='varsity',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=64),
        ),
    ]
