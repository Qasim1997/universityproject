# Generated by Django 3.2.7 on 2021-09-24 05:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0013_auto_20210924_0537'),
    ]

    operations = [
        migrations.AddField(
            model_name='detail',
            name='hotel',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='home.hotel'),
        ),
    ]