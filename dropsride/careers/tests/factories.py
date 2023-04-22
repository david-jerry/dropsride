import factory
from countries_plus.models import Country
from django.test import TestCase
from django.utils.text import slugify
from factory.django import DjangoModelFactory

from dropsride.careers.models import Applicants, Careers, Teams
from dropsride.settings.models import Localization


class TeamsFactory(DjangoModelFactory):
    class Meta:
        model = Teams

    title = factory.Faker("sentence", nb_words=3)
    slug = factory.LazyAttribute(lambda o: slugify(o.title))


class TeamsTestCase(TestCase):
    def setUp(self):
        self.team = TeamsFactory.create()

    def test_teams_model(self):
        team = self.team
        self.assertTrue(isinstance(team, Teams))
        self.assertEqual(team.__str__(), team.title.title())
        self.assertEqual(team.get_absolute_url(), f"/careers/department/{team.slug}/")
        self.assertEqual(
            self.team.get_absolute_url(),
            f"/teams/{self.team.slug}/",
            msg="Wrong URL returned",
        )


class CareersFactory(DjangoModelFactory):
    class Meta:
        model = Careers

    title = factory.Sequence(lambda n: f"Career {n}")
    description = "Join our team as a software engineer"
    requirements = "At least 2 years of experience"
    location = factory.SubFactory(TeamsFactory)
    salary = 100000


class CareersTestCase(TestCase):
    def setUp(self):
        self.career = CareersFactory.create()

    def test_careers_model(self):
        c = self.career
        self.assertTrue(isinstance(c, Careers))
        self.assertEqual(c.__str__(), c.title.title())
        self.assertEqual(c.get_absolute_url(), f"/careers/{c.slug}/")
        self.assertEqual(
            c.get_absolute_url(),
            f"/career/{c.slug}/",
            msg="Wrong URL returned",
        )


class LocalizationFactory(DjangoModelFactory):
    class Meta:
        model = Localization

    city = "New York"
    state = "NY"
    country = "United States"


class ApplicantsFactory(DjangoModelFactory):
    class Meta:
        model = Applicants

    position = factory.SubFactory(CareersFactory)
    first_name = "John"
    middle_name = "Doe"
    last_name = "Smith"
    email = "john.smith@gmail.com"
    phone_number = "1234567890"
    gender = "male"
    age = 25
    location = factory.SubFactory(LocalizationFactory)
    cover_letter = "I am interested in this position"
    disability = True
    consent = True
    country = "US"


class ApplicantsTestCase(TestCase):
    def setUp(self):
        self.applicant = ApplicantsFactory.create()

    def test_careers_model(self):
        a = self.applicant
        self.assertTrue(isinstance(a, Applicants))
        self.assertEqual(a.__str__(), a.title.title())
        self.assertEqual(a.get_absolute_url(), f"/careers/{a.slug}/")
        self.assertEqual(
            a.get_absolute_url(),
            f"/career/{a.slug}/",
            msg="Wrong URL returned",
        )
