# Generated by Django 3.0.3 on 2020-03-05 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dbapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='img',
            field=models.ImageField(default=2, upload_to='imgs/'),
            preserve_default=False,
        ),
    ]
