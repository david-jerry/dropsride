# Generated by Django 4.0.10 on 2023-05-04 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_user_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='verifieddocuments',
            name='license',
            field=models.CharField(blank=True, db_index=True, max_length=50, null=True, verbose_name='Drivers License'),
        ),
    ]