# Generated by Django 3.0.8 on 2021-07-25 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0003_notification_n_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='slug',
            field=models.SlugField(default='djangodbmodelsfieldscharfield', max_length=255, unique=False),
        ),
    ]
