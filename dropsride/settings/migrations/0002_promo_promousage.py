# Generated by Django 4.0.10 on 2023-04-28 11:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('settings', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Promo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('name', models.CharField(max_length=100)),
                ('code', models.CharField(max_length=8)),
                ('description', models.TextField()),
                ('discount_percent', models.DecimalField(decimal_places=2, max_digits=5)),
                ('discount_rides', models.IntegerField()),
                ('rides_count', models.IntegerField()),
                ('usage_count', models.IntegerField()),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PromoUsage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('used', models.BooleanField(default=False)),
                ('used_date', models.DateTimeField(blank=True, null=True)),
                ('promo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='promo_subscribers', to='settings.promo')),
                ('subscriber', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='promo_subscribers', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('promo', 'subscriber')},
            },
        ),
    ]