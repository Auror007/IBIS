# Generated by Django 2.2 on 2019-04-06 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ibis', '0003_birds_info_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='birds_info',
            name='image',
            field=models.ImageField(blank=True, upload_to='birds_image'),
        ),
    ]
