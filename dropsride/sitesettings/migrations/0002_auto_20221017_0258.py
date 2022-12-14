# Generated by Django 3.2.15 on 2022-10-17 01:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sitesettings', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='localization',
            name='head_office',
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AddField(
            model_name='localization',
            name='office_phone_1',
            field=models.CharField(blank=True, max_length=14),
        ),
        migrations.AddField(
            model_name='localization',
            name='office_phone_2',
            field=models.CharField(blank=True, max_length=14),
        ),
        migrations.AddField(
            model_name='localization',
            name='rep',
            field=models.CharField(blank=True, max_length=250),
        ),
    ]
