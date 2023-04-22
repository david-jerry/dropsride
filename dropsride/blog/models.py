import readtime
from django.conf import settings
from django.db.models import (
    CASCADE,
    BooleanField,
    CharField,
    DateField,
    ForeignKey,
    Manager,
    SlugField,
)
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from model_utils.models import TimeStampedModel
from stdimage import StdImageField
from taggit.managers import TaggableManager
from tinymce.models import HTMLField

from dropsride.blog.managers import NewsManager

User = settings.AUTH_USER_MODEL


class News(TimeStampedModel):
    """
    This is a model for blog contents wards for children will read.
    """

    image = StdImageField(
        _("Post Cover Photo"),
        upload_to="reads/cover",
        blank=True,
        delete_orphans=True,
        variations={"thumbnail": {"width": 100, "height": 100, "crop": True}},
    )
    title = CharField(_("Post Title"), blank=True, max_length=160)
    summary = HTMLField(_("Post Summary"), blank=True, max_length=255)
    keywords = CharField(_("Post Keywords"), blank=True, max_length=500)
    content = HTMLField(_("Post Content"), blank=False)

    published_date = DateField(null=True, blank=True, db_index=True)

    author = ForeignKey(
        User,
        on_delete=CASCADE,
        blank=True,
        null=True,
        default=None,
        related_name="news_author",
        db_index=True,
    )
    publisher = CharField(max_length=255, default="Dropsride Publishers")

    slug = SlugField(_("Slug"), blank=True, max_length=500, db_index=True)

    draft = BooleanField(_("Draft/Published"), default=True)
    featured = BooleanField(_("Featured Post"), default=False)

    tags = TaggableManager()

    objects = Manager()
    published = NewsManager()

    def __str__(self):
        return self.title.title()

    class Meta:
        managed = True
        verbose_name = "Blog"
        verbose_name_plural = "Blogs"
        ordering = ["-published_date"]

    def related_articles(self):
        return self.tags.similar_objects()

    @property
    def get_readtime(self):
        # readtime.of_markdown(self.content) or readtime.of_text(self.content)
        return readtime.of_html(self.content)

    def get_next(self):
        next = self.__class__.objects.filter(
            draft=False, published_date__gt=self.published_date
        ).order_by("-published_date")
        try:
            return next[0]
        except IndexError:
            return None

    def get_prev(self):
        prev = self.__class__.objects.filter(
            draft=False, published_date__lt=self.published_date
        ).order_by("-published_date")
        try:
            return prev[0]
        except IndexError:
            return None

    def get_share_url(self):
        if settings.PRODUCTION:
            return f"https://dropsride.com/{self.get_absolute_url()}"
        else:
            return f"http://localhost:8000/{self.get_absolute_url()}"

    def get_absolute_url(self):
        """
        Returns the url to access a particular instance of blog post.
        """
        return reverse("news:detail", kwargs={"slug": self.slug})
