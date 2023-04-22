import io

from countries_plus.models import Country
from django.core.files.uploadedfile import SimpleUploadedFile
from django.urls import reverse
from PIL import Image
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient, APITestCase

from dropsride.careers.api.serializers import (
    ApplicantSerializer,
    CareerSerializer,
    TeamSerializer,
)
from dropsride.careers.models import Applicants, Careers, Teams
from dropsride.settings.models import Localization


class TeamViewSetTestCase(APITestCase):
    def setUp(self):
        self.team1 = Teams.objects.create(name="Team 1")
        self.team2 = Teams.objects.create(name="Team 2")

    def test_list_teams(self):
        response = self.client.get("/api/teams/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        serializer_data = TeamSerializer([self.team1, self.team2], many=True).data
        self.assertEqual(response.data, serializer_data)

    def test_retrieve_team(self):
        response = self.client.get(f"/api/teams/{self.team1.pk}/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        serializer_data = TeamSerializer(self.team1).data
        self.assertEqual(response.data, serializer_data)

    def test_create_team(self):
        data = {"name": "Team 3"}
        response = self.client.post("/api/teams/", data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        team = Teams.objects.get(name=data["name"])
        serializer_data = TeamSerializer(team).data
        self.assertEqual(response.data, serializer_data)

    def test_update_team(self):
        data = {"name": "Team 1 updated"}
        response = self.client.put(f"/api/teams/{self.team1.pk}/", data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        team = Teams.objects.get(pk=self.team1.pk)
        self.assertEqual(team.name, data["name"])

    def test_partial_update_team(self):
        data = {"name": "Team 1 updated again"}
        response = self.client.patch(f"/api/teams/{self.team1.pk}/", data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        team = Teams.objects.get(pk=self.team1.pk)
        self.assertEqual(team.name, data["name"])

    def test_delete_team(self):
        response = self.client.delete(f"/api/teams/{self.team1.pk}/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        with self.assertRaises(Teams.DoesNotExist):
            Teams.objects.get(pk=self.team1.pk)


class ApplicantViewSetTestCase(APITestCase):
    def setUp(self):
        self.localization = Localization.objects.create(name="Test Localization")
        self.country = Country.objects.create(name="Test Country", iso="TC")
        self.applicant1 = Applicants.objects.create(
            first_name="John",
            last_name="Doe",
            email="john.doe@example.com",
            phone_number="1234567890",
            gender="M",
            age=25,
            location=self.localization,
            file="test_file.txt",
            cover_letter="Test cover letter",
            disability=True,
            consent=True,
            country=self.country,
        )
        self.applicant2 = Applicants.objects.create(
            first_name="Jane",
            last_name="Doe",
            email="jane.doe@example.com",
            phone_number="0987654321",
            gender="F",
            age=30,
            location=self.localization,
            file="test_file2.txt",
            cover_letter="Test cover letter 2",
            disability=False,
            consent=False,
            country=self.country,
        )

    def test_list_applicants(self):
        response = self.client.get("/api/applicants/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
        serializer_data = ApplicantSerializer(
            [self.applicant1, self.applicant2], many=True
        ).data
        self.assertEqual(response.data, serializer_data)

    def test_retrieve_applicant(self):
        response = self.client.get(f"/api/applicants/{self.applicant1.pk}/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["first_name"], "John")
        self.assertEqual(response.data["last_name"], "Doe")
        self.assertEqual(response.data["email"], "john.doe@example.com")
        self.assertEqual(response.data["phone_number"], "1234567890")
        self.assertEqual(response.data["gender"], "M")
        self.assertEqual(response.data["age"], 25)
        self.assertEqual(response.data["location"]["name"], "Test Localization")
        self.assertEqual(response.data["file"], "test_file.txt")
        self.assertEqual(response.data["cover_letter"], "Test cover letter")
        self.assertEqual(response.data["disability"], True)
        self.assertEqual(response.data["consent"], True)
        self.assertEqual(response.data["country"]["name"], "Test Country")
        self.assertEqual(response.data["country"]["iso"], "TC")

    def test_create_applicant(self):
        data = {
            "first_name": "Jane",
            "last_name": "Doe",
            "email": "jane.doe@example.com",
            "phone_number": "0987654321",
            "gender": "F",
            "age": 30,
            "location": self.localization.uuid,
            "file": "test_file3.txt",
            "cover_letter": "Test cover letter 3",
            "disability": False,
            "consent": True,
            "country": self.country.iso,
        }
        response = self.client.post("/api/applicants/", data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Applicants.objects.count(), 3)

    def test_update_applicant(self):
        data = {
            "first_name": "Johny",
            "last_name": "Doe",
            "email": "john.doe@example.com",
            "phone_number": "1234567890",
            "gender": "M",
            "age": 26,
            "location": self.localization.uuid,
            "file": "test_file_updated.txt",
            "cover_letter": "Test cover letter updated",
            "disability": False,
            "consent": True,
            "country": self.country.iso,
        }
        response = self.client.put(f"/api/applicants/{self.applicant1.pk}/", data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.applicant1.refresh_from_db()
        self.assertEqual(self.applicant1.first_name, "Johny")
        self.assertEqual(self.applicant1.age, 26)
        self.assertEqual(self.applicant1.file, "test_file_updated.txt")
        self.assertEqual(self.applicant1.cover_letter, "Test cover letter updated")

    def test_delete_applicant(self):
        response = self.client.delete(f"/api/applicants/{self.applicant1.pk}/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Applicants.objects.count(), 1)


class CareerViewSetTests(APITestCase):
    def setUp(self):
        self.local = Localization.objects.create(
            city="New York", state="NY", country="United States"
        )
        self.country = Country.objects.create(name="United States", iso="US")
        self.career = Careers.objects.create(
            title="Software Engineer",
            description="Join our team as a software engineer",
            requirements="At least 2 years of experience",
            location=self.local,
            country=self.country,
            salary=100000,
        )
        self.token = Token.objects.create(user=self.user)
        self.api_authentication()

    def api_authentication(self):
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token.key)

    def test_apply_to_career(self):
        url = reverse("career-apply", args=[self.career.slug])
        image = Image.new("RGB", (100, 100), color="red")
        file = io.BytesIO()
        image.save(file, "jpeg")
        file = SimpleUploadedFile(
            "test.jpeg", file.getvalue(), content_type="image/jpeg"
        )
        data = {
            "first_name": "John",
            "middle_name": "Doe",
            "last_name": "Smith",
            "email": "john.smith@gmail.com",
            "phone_number": "1234567890",
            "gender": "male",
            "age": 25,
            "location": self.local.uuid,
            "file": file,
            "cover_letter": "I am interested in this position",
            "disability": "on",
            "consent": "on",
            "country": self.country.iso,
        }
        response = self.client.post(url, data, format="multipart")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Applicants.objects.count(), 1)
        applicant = Applicants.objects.get()
        self.assertEqual(applicant.position, self.career)
        self.assertEqual(applicant.first_name, "John")
        self.assertEqual(applicant.middle_name, "Doe")
        self.assertEqual(applicant.last_name, "Smith")
        self.assertEqual(applicant.email, "john.smith@gmail.com")
        self.assertEqual(applicant.phone_number, "1234567890")
        self.assertEqual(applicant.gender, "male")
        self.assertEqual(applicant.age, 25)
        self.assertEqual(applicant.location, self.local)
        self.assertEqual(applicant.file.name, "test.jpeg")
        self.assertEqual(applicant.cover_letter, "I am interested in this position")
        self.assertEqual(applicant.disability, True)
        self.assertEqual(applicant.consent, True)
        self.assertEqual(applicant.country, self.country)

    def test_apply_to_career_without_file(self):
        url = reverse("career-apply", args=[self.career.slug])
        data = {
            "first_name": "John",
            "middle_name": "Doe",
            "last_name": "Smith",
            "email": "john.smith@gmail.com",
            "phone_number": "1234567890",
            "gender": "male",
            "age": 25,
            "location": self.local.uuid,
            "cover_letter": "I am interested in this position",
            "disability": "on",
            "consent": "on",
            "country": self.country.iso,
        }
        response = self.client.post(url, data, format="multipart")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Applicants.objects.count(), 0)

    def test_apply_to_career_with_invalid_data(self):
        url = reverse("career-apply", args=[self.career.slug])
        data = {
            "first_name": "John",
            "middle_name": "Doe",
            "last_name": "Smith",
            "email": "john.smith@gmail.com",
            "phone_number": "1234567890",
            "gender": "male",
            "age": -1,  # Invalid age
            "location": self.local.uuid,
            "file": None,  # Missing file
            "cover_letter": "",  # Empty cover letter
            "disability": "on",
            "consent": "on",
            "country": "USA",  # Invalid country ISO code
        }
        response = self.client.post(url, data, format="multipart")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Applicants.objects.count(), 0)
