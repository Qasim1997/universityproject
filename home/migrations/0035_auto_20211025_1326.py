# Generated by Django 3.1.4 on 2021-10-25 08:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0034_auto_20211025_0942'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='ordered_date',
            new_name='book_date',
        ),
    ]
