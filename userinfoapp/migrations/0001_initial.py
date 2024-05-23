# Generated by Django 5.0.2 on 2024-03-12 16:56

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='userInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('goal', models.CharField(max_length=255)),
                ('gender', models.CharField(max_length=255)),
                ('age', models.DecimalField(decimal_places=0, max_digits=2)),
                ('weight', models.DecimalField(decimal_places=2, max_digits=3)),
                ('current_mood', models.CharField(max_length=255)),
                ('past_medical_help', models.BooleanField(default=False)),
                ('physical_stress', models.BooleanField(default=True)),
                ('sleep_quality', models.CharField(max_length=255)),
                ('medications', models.CharField(max_length=255)),
                ('stress_level', models.DecimalField(decimal_places=0, max_digits=1)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]