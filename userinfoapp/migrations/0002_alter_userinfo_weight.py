# Generated by Django 5.0.2 on 2024-03-12 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userinfoapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='weight',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
    ]
