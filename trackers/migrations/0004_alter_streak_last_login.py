# Generated by Django 5.0.2 on 2024-03-19 07:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trackers', '0003_alter_streak_last_login'),
    ]

    operations = [
        migrations.AlterField(
            model_name='streak',
            name='last_login',
            field=models.DateField(default=datetime.date(2024, 3, 19)),
        ),
    ]
