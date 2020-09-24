# Generated by Django 3.0.6 on 2020-06-10 07:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Donor', '0003_auto_20200609_2141'),
    ]

    operations = [
        migrations.CreateModel(
            name='Acknowledge',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('body', models.TextField(max_length=255)),
                ('photo', models.ImageField(upload_to='')),
                ('created', models.DateTimeField(blank=True, default=datetime.datetime(2020, 6, 10, 0, 48, 26, 834271))),
            ],
        ),
        migrations.AlterModelOptions(
            name='donors',
            options={'verbose_name_plural': 'Donors'},
        ),
        migrations.AlterField(
            model_name='donors',
            name='created',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 6, 10, 0, 48, 26, 831772)),
        ),
    ]
