# Generated by Django 3.2.15 on 2022-09-30 07:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('countries_plus', '0005_auto_20160224_1804'),
        ('users', '0002_auto_20220930_0400'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='country',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='countries_plus.country', verbose_name='Country'),
        ),
        migrations.AddField(
            model_name='user',
            name='date_of_birth',
            field=models.DateField(blank=True, null=True, verbose_name='Date of birth'),
        ),
        migrations.AddField(
            model_name='user',
            name='gave_consent',
            field=models.BooleanField(default=False, verbose_name="Share my registration data with readville's content providers for marketing purposes. This confirms you are up to the legal age approved in your country."),
        ),
        migrations.AddField(
            model_name='user',
            name='gender',
            field=models.CharField(blank=True, choices=[('M', 'MALE'), ('F', 'FEMALE'), ('NA', 'NONE')], default='NA', max_length=3, verbose_name='Gender'),
        ),
        migrations.AddField(
            model_name='user',
            name='ref_link',
            field=models.CharField(blank=True, max_length=500, verbose_name='Referral Link'),
        ),
    ]
