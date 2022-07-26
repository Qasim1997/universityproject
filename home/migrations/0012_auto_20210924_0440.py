# Generated by Django 3.2.7 on 2021-09-24 03:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_detail'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='detail',
            name='date',
        ),
        migrations.RemoveField(
            model_name='detail',
            name='notes',
        ),
        migrations.RemoveField(
            model_name='detail',
            name='number_of_guests',
        ),
        migrations.RemoveField(
            model_name='detail',
            name='number_of_nights',
        ),
        migrations.RemoveField(
            model_name='detail',
            name='phone_number',
        ),
        migrations.AlterField(
            model_name='detail',
            name='email',
            field=models.EmailField(max_length=30),
        ),
    ]
