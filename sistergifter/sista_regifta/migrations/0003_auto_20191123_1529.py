# Generated by Django 2.2.7 on 2019-11-23 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sista_regifta', '0002_auto_20191123_1013'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gift',
            name='date_added',
        ),
        migrations.RemoveField(
            model_name='gift',
            name='sender',
        ),
        migrations.AlterField(
            model_name='gift',
            name='gift_photo',
            field=models.ImageField(blank=True, upload_to='post_images'),
        ),
    ]