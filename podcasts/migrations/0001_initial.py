# Generated by Django 5.0.2 on 2024-03-16 03:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('hashtags', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='podcasts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('podacast_name', models.CharField(max_length=255)),
                ('podacst_description', models.CharField(max_length=255)),
                ('artist_name', models.CharField(max_length=255)),
                ('audio', models.CharField(max_length=255)),
                ('short_img', models.CharField(max_length=255)),
                ('long_img', models.CharField(max_length=255)),
                ('hashtag_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hashtags.hashtags')),
            ],
        ),
    ]
