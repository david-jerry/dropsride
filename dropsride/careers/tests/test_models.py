from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from dropsride.careers.models import Applicants, Careers, Teams
from dropsride.settings.api.serializers import LocalizationSerializer


class ModelFactoryTestCase(TestCase):
    def setUp(self):
        self.team = Teams.objects.create(title="Test Team", slug="test-team")
        self.career = Careers.objects.create(title="Test Career", team=self.team)
        self.location = LocalizationSerializer.objects.create(
            city="Test City", country="Test Country"
        )
        self.applicant = Applicants.objects.create(
            position=self.career,
            first_name="John",
            last_name="Doe",
            email="johndoe@example.com",
            phone_number="+1234567890",
            gender=Applicants.MALE,
            age=Applicants.U25,
            location=self.location,
            file="test_cv.pdf",
            cover_letter="Test cover letter",
            disability=False,
            consent=True,
            country=None,
        )

    def test_teams_model(self):
        self.assertEqual(str(self.team), "Test Team")
        self.assertQuerysetEqual(self.team.get_all_positions(), [])
        self.assertQuerysetEqual(self.team.get_all_recent_positions(), [])
        self.assertEqual(
            self.team.get_absolute_url(),
            reverse("careers:department_detail", kwargs={"slug": self.team.slug}),
        )

    def test_careers_model(self):
        self.assertEqual(str(self.career), "Test Career")
        self.assertEqual(self.career.get_next(), None)
        self.assertEqual(self.career.get_prev(), None)
        self.assertEqual(
            self.career.get_share_url(),
            f"http://localhost:8000{self.career.get_absolute_url()}",
        )
        self.assertQuerysetEqual(self.career.related_careers(), [repr(self.career)])
        self.assertEqual(self.career.get_applicants, None)

    def test_applicants_model(self):
        self.assertEqual(
            str(self.applicant),
            "John Doe | johndoe@example.com | Test Career | Test City",
        )
        self.assertEqual(self.applicant.get_fullname, "John Doe ")
        self.assertEqual(
            self.applicant.get_absolute_url(),
            reverse("careers:detail", kwargs={"slug": self.career.slug}),
        )
