# Generated by Django 4.0.10 on 2023-04-28 21:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0002_promo_promousage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='promo',
            name='code',
            field=models.CharField(blank=True, max_length=8),
        ),
        migrations.AlterField(
            model_name='promo',
            name='discount_rides',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
    ]
