# Generated by Django 3.2.15 on 2022-10-05 14:10

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields
import stdimage.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('drivers', '0002_auto_20221005_1510'),
    ]

    operations = [
        migrations.CreateModel(
            name='Documents',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('document_type', models.CharField(max_length=150)),
                ('document', stdimage.models.StdImageField(upload_to='')),
                ('approved', models.BooleanField(default=False)),
                ('driver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='drivers_licence', to='drivers.drivers')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
