# Generated by Django 2.1.1 on 2018-10-13 17:05

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('guestbook', '0003_auto_20181014_0034'),
    ]

    operations = [
        migrations.AddField(
            model_name='textmessage',
            name='date_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
