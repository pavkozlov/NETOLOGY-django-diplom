# Generated by Django 2.2.3 on 2019-07-23 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0009_auto_20190720_0918'),
    ]

    operations = [
        migrations.AddField(
            model_name='basket',
            name='username',
            field=models.CharField(blank=True, max_length=150),
        ),
        migrations.AlterField(
            model_name='basket',
            name='sid',
            field=models.CharField(blank=True, max_length=150),
        ),
    ]
