# Generated by Django 3.0.6 on 2020-06-21 01:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pandemic', '0008_auto_20200619_0942'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faq',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 6, 20, 18, 48, 47, 281508)),
        ),
    ]
