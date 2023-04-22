from django.urls import resolve, reverse

from dropsride.careers.models import Applicants, Careers, Teams


def test_team_detail(team: Teams):
    assert (
        reverse("api:team-detail", kwargs={"pk": team.pk}) == f"/api/teams/{team.pk}/"
    )
    assert resolve(f"/api/teams/{team.pk}/").view_name == "api:team-detail"


def test_team_list():
    assert reverse("api:team-list") == "/api/teams/"
    assert resolve("/api/teams/").view_name == "api:team-list"


def test_team_destroy(team: Teams):
    assert (
        reverse("api:team-destroy", kwargs={"pk": team.pk})
        == f"/api/teams/{team.pk}/destroy/"
    )
    assert resolve(f"/api/teams/{team.pk}/destroy/").view_name == "api:team-destroy"
