# Generated by Django 5.0.2 on 2024-03-16 02:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('execises', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exercises',
            name='calories',
            field=models.DecimalField(decimal_places=0, max_digits=3),
        ),
    ]
