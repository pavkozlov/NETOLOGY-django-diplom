# Generated by Django 2.2.3 on 2019-07-19 13:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0007_auto_20190718_2018'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='start',
            new_name='star',
        ),
    ]
