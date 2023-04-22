from django.contrib.auth.models import User
from django.test import RequestFactory, TestCase
from django.urls import reverse
from mixer.backend.django import mixer

from dropsride.careers.forms import ApplicantsForm
from dropsride.careers.models import Applicants, Careers, Teams
from dropsride.careers.views import (
    CareerDetailView,
    CareerListView,
    CareerUpdateView,
    DepartmentCreateView,
    DepartmentDetailView,
    DepartmentUpdateView,
    applicant_create,
    applicant_detail,
    department_list,
)


class TestCareerListView(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(
            username="testuser", email="testuser@example.com", password="password"
        )
        self.team = mixer.blend(Teams)
        self.career = mixer.blend(
            Careers, team=self.team, title="Test Career", draft=False
        )

    def test_career_list_view_with_authentication(self):
        url = reverse("careers:list")
        request = self.factory.get(url, data={"search": "Test Career"})
        request.user = self.user
        response = CareerListView.as_view()(request)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Career")
        self.assertTemplateUsed(response, "admin/careers/list.html")

    def test_career_list_view_without_authentication(self):
        url = reverse("careers:list")
        request = self.factory.get(url, data={"search": "Test Career"})
        response = CareerListView.as_view()(request)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Career")
        self.assertTemplateUsed(response, "careers/list.html")


class TestCareerDetailView(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(
            username="testuser", email="testuser@example.com", password="password"
        )
        self.team = mixer.blend(Teams)
        self.career = mixer.blend(
            Careers, team=self.team, title="Test Career", draft=False
        )

    def test_career_detail_view_with_authentication(self):
        url = reverse("careers:detail", kwargs={"slug": self.career.slug})
        request = self.factory.get(url)
        request.user = self.user
        response = CareerDetailView.as_view()(request, slug=self.career.slug)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Career")
        self.assertTemplateUsed(response, "careers/detail.html")

    def test_career_detail_view_without_authentication(self):
        url = reverse("careers:detail", kwargs={"slug": self.career.slug})
        request = self.factory.get(url)
        response = CareerDetailView.as_view()(request, slug=self.career.slug)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Career")
        self.assertTemplateUsed(response, "careers/detail.html")


class TestCareerUpdateView(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(
            username="testuser", email="testuser@example.com", password="password"
        )
        self.team = mixer.blend(Teams)
        self.career = mixer.blend(
            Careers, team=self.team, title="Test Career", draft=False
        )

    def test_career_update_view_with_authentication(self):
        url = reverse("careers:update", kwargs={"slug": self.career.slug})
        request = self.factory.get(url)
        request.user = self.user
        response = CareerUpdateView.as_view()(request, slug=self.career.slug)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Career")
        self.assertTemplateUsed(response, "admin/careers/form.html")

    def test_career_update_view_without_authentication(self):
        url = reverse("careers:update", kwargs={"slug": self.career.slug})
        request = self.factory.get(url)
        response = CareerUpdateView.as_view()(request, slug=self.career.slug)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, "/accounts/login/?next=" + url)

    def test_career_update_view_post_with_authentication(self):
        url = reverse("careers:update", kwargs={"slug": self.career.slug})
        data = {
            "title": "Test Career Updated",
            "description": "This is an updated description.",
            "team": self.team.pk,
            "draft": True,
        }
        request = self.factory.post(url, data=data)
        request.user = self.user
        response = CareerUpdateView.as_view()(request, slug=self.career.slug)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(
            response, reverse("careers:detail", kwargs={"slug": self.career.slug})
        )
        updated_career = Careers.objects.get(id=self.career.id)
        self.assertEqual(updated_career.title, "Test Career Updated")
        self.assertEqual(updated_career.description, "This is an updated description.")
        self.assertEqual(updated_career.team, self.team)
        self.assertTrue(updated_career.draft)


class DepartmentListTestCase(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(
            username="testuser", email="testuser@example.com", password="password"
        )
        self.team = mixer.blend(Teams)

    def test_department_list_view_with_authentication(self):
        url = reverse("careers:department_list")
        request = self.factory.get(url)
        request.user = self.user
        response = department_list(request)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "admin/careers/snippets/dep_list.html")

    def test_department_list_view_without_authentication(self):
        url = reverse("careers:department_list")
        request = self.factory.get(url)
        response = department_list(request)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "admin/careers/snippets/dep_list.html")


class DepartmentCreateViewTestCase(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(
            username="testuser", email="testuser@example.com", password="password"
        )
        self.department_data = {
            "name": "Test Department",
            "description": "Test description",
        }

    def test_department_create_view_with_authentication(self):
        url = reverse("careers:department_create")
        request = self.factory.post(url, data=self.department_data)
        request.user = self.user
        response = DepartmentCreateView.as_view()(request)
        self.assertEqual(response.status_code, 302)  # Should redirect after success
        self.assertRedirects(response, reverse("careers:department_list"))

    def test_department_create_view_without_authentication(self):
        url = reverse("careers:department_create")
        request = self.factory.post(url, data=self.department_data)
        response = DepartmentCreateView.as_view()(request)
        self.assertEqual(response.status_code, 302)  # Should redirect after failure
        self.assertRedirects(response, f"{reverse('account_login')}?next={url}")


class DepartmentUpdateViewTestCase(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(
            username="testuser",
            email="testuser@example.com",
            password="password",
            is_staff=True,
        )
        self.department = mixer.blend(Teams)

    def test_department_update_view_with_authentication(self):
        url = reverse(
            "careers:department_update", kwargs={"slug": self.department.slug}
        )
        request = self.factory.get(url)
        request.user = self.user
        response = DepartmentUpdateView.as_view()(request, slug=self.department.slug)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "admin/careers/snippets/dep_update.html")

    def test_department_update_view_without_authentication(self):
        url = reverse(
            "careers:department_update", kwargs={"slug": self.department.slug}
        )
        request = self.factory.get(url)
        response = DepartmentUpdateView.as_view()(request, slug=self.department.slug)
        self.assertEqual(response.status_code, 302)  # Should redirect after failure
        self.assertRedirects(response, f"{reverse('account_login')}?next={url}")


class DepartmentDetailViewTestCase(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(
            username="testuser", email="testuser@example.com", password="password"
        )
        self.department = mixer.blend(Teams)

    def test_department_detail_view_with_authentication(self):
        url = reverse(
            "careers:department_detail", kwargs={"slug": self.department.slug}
        )
        request = self.factory.get(url)
        request.user = self.user
        response = DepartmentDetailView.as_view()(request, slug=self.department.slug)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "admin/careers/dep_detail.html")

    def test_department_detail_view_without_authentication(self):
        url = reverse(
            "careers:department_detail", kwargs={"slug": self.department.slug}
        )
        request = self.factory.get(url)
        response = DepartmentDetailView.as_view()(request, slug=self.department.slug)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "careers/dep_detail.html")


class ApplicantDetailViewTestCase(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.applicant = mixer.blend(Applicants)

    def test_applicant_detail_view(self):
        url = reverse("careers:applicant_detail", kwargs={"pk": self.applicant.pk})
        request = self.factory.get(url)
        response = applicant_detail(request, pk=self.applicant.pk)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "admin/careers/app_detail.html")
        self.assertContains(response, self.applicant.full_name)


class ApplicantCreateViewTestCase(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.career = mixer.blend(Careers)

    def test_applicant_create_view(self):
        url = reverse("careers:applicant_create", kwargs={"slug": self.career.slug})
        request = self.factory.get(url)
        response = applicant_create(request, slug=self.career.slug)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "careers/snippets/app_create.html")
        self.assertContains(response, self.career.title)

        form = response.context_data["form"]
        self.assertIsInstance(form, ApplicantsForm)
