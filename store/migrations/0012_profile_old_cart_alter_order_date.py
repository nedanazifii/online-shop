# Generated by Django 5.2.3 on 2025-07-05 08:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0011_alter_order_date_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='old_cart',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2025, 7, 5, 11, 49, 27, 432013)),
        ),
    ]
