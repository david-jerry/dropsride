from django.test import SimpleTestCase, TestCase
from django.urls import resolve, reverse

from dropsride.careers.views import *


class TestUrls(SimpleTestCase):
    def test_career_list_url(self):
        url = reverse("careers:list")
        self.assertEqual(resolve(url).func, career_list)

    def test_career_create_url(self):
        url = reverse("careers:create")
        self.assertEqual(resolve(url).func, career_create)

    def test_career_pages_detail_url(self):
        url = reverse("careers:pages_detail", args=["example-slug"])
        self.assertEqual(resolve(url).func, career_pages_detail)

    def test_career_detail_url(self):
        url = reverse("careers:detail", args=["example-slug"])
        self.assertEqual(resolve(url).func, career_detail)

    def test_career_update_url(self):
        url = reverse("careers:update", args=["example-slug"])
        self.assertEqual(resolve(url).func, career_update)

    def test_department_list_url(self):
        url = reverse("careers:department_list")
        self.assertEqual(resolve(url).func, department_list)

    def test_department_create_url(self):
        url = reverse("careers:department_create")
        self.assertEqual(resolve(url).func, department_create)

    def test_department_update_url(self):
        url = reverse("careers:department_update", args=["example-slug"])
        self.assertEqual(resolve(url).func, department_update)

    def test_department_detail_url(self):
        url = reverse("careers:department_detail", args=["example-slug"])
        self.assertEqual(resolve(url).func, department_detail)

    def test_applicant_detail_url(self):
        url = reverse("careers:applicant_detail", args=[1])
        self.assertEqual(resolve(url).func, applicant_detail)

    def test_applicant_create_url(self):
        url = reverse("careers:applicant_create", args=["example-slug"])
        self.assertEqual(resolve(url).func, applicant_create)
