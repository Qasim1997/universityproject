# Generated by Django 3.2.7 on 2021-09-21 07:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_alter_hotel_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotel',
            name='city',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='home.city'),
        ),
    ]
