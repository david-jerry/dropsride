# Generated by Django 4.0.10 on 2023-04-18 07:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_rename_card_verified_savedcards_card_is_verified'),
    ]

    operations = [
        migrations.RenameField(
            model_name='savedcards',
            old_name='card_is_verified',
            new_name='card_verified',
        ),
    ]
