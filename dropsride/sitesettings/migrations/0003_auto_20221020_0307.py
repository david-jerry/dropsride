# Generated by Django 3.2.15 on 2022-10-20 02:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drivers', '0003_auto_20221018_0800'),
        ('riders', '0003_auto_20221018_0800'),
        ('sitesettings', '0002_auto_20221017_0258'),
    ]

    operations = [
        migrations.RenameField(
            model_name='localization',
            old_name='state',
            new_name='title',
        ),
        migrations.AddField(
            model_name='localization',
            name='drivers',
            field=models.ManyToManyField(to='drivers.Drivers'),
        ),
        migrations.AddField(
            model_name='localization',
            name='riders',
            field=models.ManyToManyField(to='riders.Riders'),
        ),
    ]
