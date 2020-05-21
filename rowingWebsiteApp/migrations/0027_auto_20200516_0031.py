# Generated by Django 3.0.2 on 2020-05-16 00:31

from django.db import migrations, models
import sortedm2m.fields


class Migration(migrations.Migration):

    dependencies = [
        ('rowingWebsiteApp', '0026_auto_20200515_0914'),
    ]

    operations = [
        migrations.CreateModel(
            name='Picture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(default='Picture', max_length=64)),
                ('image', models.ImageField(default='pic_folder/None/no-img.jpg', upload_to='pre-image')),
            ],
        ),
        migrations.RemoveField(
            model_name='gallery',
            name='description',
        ),
        migrations.RemoveField(
            model_name='gallery',
            name='image',
        ),
        migrations.AddField(
            model_name='gallery',
            name='photos',
            field=sortedm2m.fields.SortedManyToManyField(help_text=None, to='rowingWebsiteApp.Gallery'),
        ),
        migrations.AddField(
            model_name='gallery',
            name='title',
            field=models.CharField(default='Gallery', max_length=64),
        ),
        migrations.DeleteModel(
            name='Gallery2',
        ),
    ]