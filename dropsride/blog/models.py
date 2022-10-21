from calendar import calendar
import readtime

from django.contrib.auth.models import AbstractUser
from django.db.models import (
    CASCADE,
    DO_NOTHING,
    BooleanField,
    CharField,
    DateField,
    SlugField,
    DateTimeField,
    DecimalField,
    URLField,
    FileField,
    TextField,
    ForeignKey,
    ManyToManyField,
    ImageField,
    IntegerField,
    OneToOneField,
    PositiveSmallIntegerField,
    UUIDField,
    Sum
)
from django.contrib.contenttypes.fields import GenericRelation
from django.urls import reverse
from django.conf import settings
from django.utils.translation import gettext_lazy as _
from django.contrib.sites.models import Site

from model_utils.models import TimeStampedModel
from dropsride.blog.managers import NewsManager

from tinymce.models import HTMLField
from hitcount.models import HitCountMixin, HitCount
from stdimage import StdImageField
from taggit.managers import TaggableManager

from dropsride.admins.models import Admins

User = settings.AUTH_USER_MODEL

class News(TimeStampedModel):
    """
    This is a model to blog contents wards for children will read.
    """


    image = StdImageField(_("Post Cover Photo"), upload_to="reads/cover", blank=True, delete_orphans=True, variations={'thumbnail': {"width": 100, "height": 100, "crop": True}})
    title = CharField(_("Post Title"), blank=True, max_length=160)
    summary = HTMLField(_("Post Summary"), blank=True, max_length=255)
    keywords = CharField(_("Post Keywords"), blank=True, max_length=500)

    content = HTMLField(_("Post Content"), blank=False)

    published_date = DateField(null=True, blank=True)

    author = ForeignKey(Admins, on_delete=DO_NOTHING, blank=True, null=True, default=None, related_name="news_author")
    publisher = 'Dropsride Publishers'

    slug = SlugField(_("Slug"), blank=True, max_length=500)

    draft = BooleanField(_("Draft/Published"), default=True)
    featured = BooleanField(_("Featured Post"), default=False)

    hit_count_generic = GenericRelation(HitCount, object_id_field='object_pk', related_query_name='hit_count_generic_relation')

    tags = TaggableManager()

    objects = NewsManager()

    def __str__(self):
        return self.title.title()

    class Meta:
        managed = True
        verbose_name = "Blog"
        verbose_name_plural = "Blogs"
        ordering = ["-published_date"]

    @property
    def get_total_views(self):
        return self.hit_count_generic.hits.count()

    # @property
    # def get_total_likes(self):
    #     return self.likes.all().count()

    def related_articles(self):
        return self.tags.similar_objects()

    def get_readtime(self):
        # readtime.of_markdown(self.content) or readtime.of_text(self.content)
        return readtime.of_html(self.content)

    def get_next(self):
        next = self.__class__.objects.filter(draft=False, published_date__gt=self.published_date)
        try:
            return next[0]
        except IndexError:
            return None

    def get_prev(self):
        prev = self.__class__.objects.filter(draft=False, published_date__lt=self.published_date).order_by("-published_date")
        try:
            return prev[0]
        except IndexError:
            return None

    def get_share_url(self):
        if settings.PRODUCTION:
            return f"http://{Site.objects.get_current()}{self.get_absolute_url()}"
        else:
            return f"http://localhost:8000/{self.get_absolute_url()}"

    def get_absolute_url(self):
        """
        Returns the url to access a particular instance of blog post.
        """
        return reverse("news:detail", kwargs={"slug": self.slug})


