# Generated by Django 4.0.10 on 2023-04-11 17:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('tickets', '0001_initial'),
        ('settings', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='ticketsubscription',
            name='driver',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='driver_subscription', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='ticketsubscription',
            name='plan',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='plan', to='tickets.ticketplans'),
        ),
        migrations.AddField(
            model_name='ticketplans',
            name='localization',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='localization', to='settings.localization'),
        ),
    ]