# Generated by Django 3.1.7 on 2021-04-05 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weaver_api', '0004_auto_20210405_1336'),
    ]

    operations = [
        migrations.AddField(
            model_name='weavedimage',
            name='image_creation_time',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='weavedimage',
            name='image_url',
            field=models.URLField(),
        ),
    ]
