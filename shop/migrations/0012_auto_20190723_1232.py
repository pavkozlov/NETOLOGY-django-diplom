# Generated by Django 2.2.3 on 2019-07-23 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0011_order_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basket',
            name='sid',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='basket',
            name='username',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]
