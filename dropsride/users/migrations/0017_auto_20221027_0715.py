# Generated by Django 3.2.15 on 2022-10-27 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0016_auto_20221027_0144'),
    ]

    operations = [
        migrations.AlterField(
            model_name='savedcards',
            name='card_exp_month',
            field=models.PositiveBigIntegerField(blank=True, max_length=2),
        ),
        migrations.AlterField(
            model_name='savedcards',
            name='card_exp_year',
            field=models.PositiveBigIntegerField(blank=True, max_length=4),
        ),
    ]
