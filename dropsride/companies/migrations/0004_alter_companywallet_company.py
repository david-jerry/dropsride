# Generated by Django 3.2.15 on 2022-10-26 04:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0003_auto_20221025_1725'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companywallet',
            name='company',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='company_wallet', to='companies.company'),
        ),
    ]
