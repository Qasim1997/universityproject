# Generated by Django 3.2.7 on 2021-09-24 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0020_remove_detail_hotel'),
    ]

    operations = [
        migrations.AddField(
            model_name='detail',
            name='password',
            field=models.CharField(max_length=75, null=True),
        ),
    ]
