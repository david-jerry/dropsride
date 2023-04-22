from countries_plus.models import Country
from django.conf import settings
from django.contrib.sites.models import Site
from django.db.models import (
    CASCADE,
    BooleanField,
    CharField,
    DateField,
    DecimalField,
    EmailField,
    FileField,
    ForeignKey,
    Manager,
    ManyToManyField,
    SlugField,
)
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from model_utils.models import TimeStampedModel
from tinymce.models import HTMLField

# from hitcount.models import HitCountMixin, HitCount
from dropsride.careers.managers import CareersManager
from dropsride.settings.models import Localization
from dropsride.utils.validators import validate_uploaded_pdf_extension

User = settings.AUTH_USER_MODEL


class Teams(TimeStampedModel):
    title = CharField(blank=True, max_length=255)
    slug = SlugField(_("Slug"), blank=True, max_length=500, db_index=True)

    def __str__(self) -> str:
        return self.title.title()

    def get_all_positions(self):
        return self.careers_set.filter(draft=False)

    def get_all_recent_positions(self):
        return self.careers_set.get_recent_careers().filter(draft=False)

    def get_absolute_url(self):
        """
        Returns the url to access a particular instance of careers post.
        """
        return reverse("careers:department_detail", kwargs={"slug": self.slug})

    class Meta:
        managed = True
        verbose_name = "Department"
        verbose_name_plural = "Departments"
        ordering = ["title"]


class Careers(TimeStampedModel):
    """
    This is a model to blog contents wards for children will read.
    """

    title = CharField(_("Career Title"), blank=True, max_length=160)
    summary = HTMLField(_("Career Summary"), blank=True, max_length=255)
    keywords = CharField(_("Career Keywords"), blank=True, max_length=500)
    team = ForeignKey(Teams, on_delete=CASCADE, db_index=True)
    location = ManyToManyField(Localization)
    salary = DecimalField(default=0.00, decimal_places=2, max_digits=20)
    competency = CharField(blank=True, max_length=255)
    content = HTMLField(_("Career Content"), blank=False)
    published_date = DateField(null=True, blank=True, db_index=True)
    slug = SlugField(_("Slug"), blank=True, max_length=500, db_index=True)
    draft = BooleanField(_("Draft/Published"), default=True)

    objects = Manager()
    published = CareersManager()

    def __str__(self) -> str:
        return self.title.title()

    class Meta:
        managed = True
        verbose_name = "Careers"
        verbose_name_plural = "Careers"
        ordering = ["-published_date", "-modified"]

    def related_careers(self):
        return self.__class__.objects.select_related("team").filter(team=self.team)

    @property
    def get_applicants(self):
        if self.job_position:
            return self.job_position.all()
        return None

    def get_next(self):
        next = self.__class__.objects.filter(
            draft=False, published_date__gt=self.published_date
        )
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
            return f"http://{Site.objects.get_current()}{self.get_absolute_url()}"
        else:
            return f"http://localhost:8000/{self.get_absolute_url()}"

    def get_absolute_url(self):
        """
        Returns the url to access a particular instance of careers post.
        """
        return reverse("careers:detail", kwargs={"slug": self.slug})


class Applicants(TimeStampedModel):
    MALE = "MALE"
    FEMALE = "FEMALE"
    NON_BINARY = "NON-BINARY"
    GENDER = ((MALE, MALE), (FEMALE, FEMALE), (NON_BINARY, NON_BINARY))

    U21 = "U21"
    U25 = "U25"
    U34 = "U34"
    U44 = "U44"
    U54 = "U54"
    U64 = "U64"
    O65 = "O65"
    AGE = (
        (U21, U21),
        (U25, U25),
        (U34, U34),
        (U44, U44),
        (U54, U54),
        (U64, U64),
        (O65, O65),
    )

    position = ForeignKey(
        Careers, on_delete=CASCADE, related_name="job_position", db_index=True
    )

    first_name = CharField(blank=True, max_length=500)
    middle_name = CharField(blank=True, max_length=500)
    last_name = CharField(blank=True, max_length=500)
    email = EmailField()
    phone_number = CharField(max_length=15)
    gender = CharField(choices=GENDER, default=NON_BINARY, max_length=15)
    age = CharField(choices=AGE, max_length=6, default=U21)

    location = ForeignKey(Localization, on_delete=CASCADE, db_index=True)

    file = FileField(
        upload_to="applicants/cv",
        validators=[validate_uploaded_pdf_extension],
        blank=False,
        null=False,
    )
    cover_letter = HTMLField()

    disability = BooleanField(default=False)
    consent = BooleanField(default=False)

    country = ForeignKey(
        Country,
        on_delete=CASCADE,
        verbose_name=_("Country"),
        blank=True,
        null=True,
        db_index=True,
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name} | {self.email} | {self.position.title} | {self.location.state.state.title()}"

    class Meta:
        managed = True
        verbose_name = "Applicant"
        verbose_name_plural = "Applicants"
        ordering = ["-modified"]

    @property
    def get_fullname(self):
        return f"{self.first_name} {self.middle_name} {self.last_name}"

    def get_absolute_url(self):
        """
        Returns the url to access a particular instance of careers post.
        """
        return reverse("career:applicant", kwargs={"pk": self.id})
