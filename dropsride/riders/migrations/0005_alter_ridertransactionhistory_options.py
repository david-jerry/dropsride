# Generated by Django 3.2.15 on 2022-10-25 16:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('riders', '0004_auto_20221025_1417'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ridertransactionhistory',
            options={'managed': True, 'ordering': ['-created'], 'verbose_name': 'Rider Transaction History', 'verbose_name_plural': 'Riders Transaction Histories'},
        ),
    ]
