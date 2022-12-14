# Generated by Django 3.2.15 on 2022-10-17 01:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields
import stdimage.models
import taggit.managers
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('admins', '0001_initial'),
        ('taggit', '0005_auto_20220424_2025'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('image', stdimage.models.StdImageField(blank=True, upload_to='reads/cover', verbose_name='Post Cover Photo')),
                ('title', models.CharField(blank=True, max_length=160, verbose_name='Post Title')),
                ('summary', tinymce.models.HTMLField(blank=True, max_length=255, verbose_name='Post Summary')),
                ('keywords', models.CharField(blank=True, max_length=500, verbose_name='Post Keywords')),
                ('content', tinymce.models.HTMLField(verbose_name='Post Content')),
                ('published_date', models.DateField(blank=True, null=True)),
                ('audio', models.FileField(blank=True, null=True, upload_to='reads/audio')),
                ('slug', models.SlugField(blank=True, max_length=500, verbose_name='Slug')),
                ('draft', models.BooleanField(default=True, verbose_name='Draft/Published')),
                ('author', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='news_author', to='admins.admins')),
                ('likes', models.ManyToManyField(blank=True, default=None, related_name='news_likes', to=settings.AUTH_USER_MODEL)),
                ('tags', taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags')),
            ],
            options={
                'verbose_name': 'Blog',
                'verbose_name_plural': 'Blogs',
                'ordering': ['-published_date'],
                'managed': True,
            },
        ),
    ]
