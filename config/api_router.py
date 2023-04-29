# from dj_rest_auth.views import PasswordResetView, PasswordResetConfirmView
from dj_rest_auth.registration.views import (  # VerifyEmailView,; ConfirmEmailView,
    SocialAccountDisconnectView,
    SocialAccountListView,
)
from django.conf import settings
from django.urls import include, path
from rest_framework.routers import DefaultRouter, SimpleRouter

from dropsride.blog.api.views import NewsViewset, TagViewset
from dropsride.careers.api.views import ApplicantViewSet, CareerViewSet, TeamViewSet
from dropsride.core.api.views import ContactView
from dropsride.currency.api.views import BanksViewSet, CurrencyViewSet, StatesViewSet
from dropsride.settings.api.views import (
    CartypeViewset,
    LocalizationViewset,
    PromoViewSet,
)
from dropsride.tickets.api.views import PlansViewset, SubscriptionViewset
from dropsride.transactions.api.views import TransactionViewSet
from dropsride.users.api.views import (
    NextOfKinViewSet,
    RegisteredVehiclesViewSet,
    SavedCardsViewSet,
    SettingsViewSet,
    UserViewSet,
    VerifiedDocumentsViewSet,
)
from dropsride.users.views import FacebookLogin, GoogleLogin

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()


router.register("tags", TagViewset, basename="tag")
router.register("news", NewsViewset, basename="news")

router.register("teams", TeamViewSet, basename="department")
router.register("applicants", ApplicantViewSet, basename="applicant")
router.register("careers", CareerViewSet, basename="career")

router.register("subscriptions", SubscriptionViewset, basename="subscription")
router.register("transactions", TransactionViewSet, basename="transaction")
router.register("localizations", LocalizationViewset, basename="localization")
router.register("cartypes", CartypeViewset, basename="cartype")
router.register("promos", PromoViewSet, basename="promo")

router.register("settings", SettingsViewSet)
router.register("nok", NextOfKinViewSet)
router.register("vehicles", RegisteredVehiclesViewSet)
router.register("documents", VerifiedDocumentsViewSet)

router.register("banks", BanksViewSet)
router.register("cards", SavedCardsViewSet)

router.register("currencies", CurrencyViewSet)
router.register("plans", PlansViewset)
router.register("states", StatesViewSet)
# router.register('support', ContactView)

router.register("users", UserViewSet, basename="user")

app_name = "api"
urlpatterns = router.urls

urlpatterns += [
    path("support/", ContactView.as_view(), name="support"),
    path("auth/", include("dj_rest_auth.urls")),
    path(
        "auth/socialaccounts/",
        SocialAccountListView.as_view(),
        name="social_account_list",
    ),
    path(
        "auth/socialaccounts/<pk>/disconnect/",
        SocialAccountDisconnectView.as_view(),
        name="social_account_disconnect",
    ),
    path("auth/registration/", include("dj_rest_auth.registration.urls")),
    path("auth/facebook/login/", FacebookLogin.as_view(), name="fb_login"),
    path("auth/google/login/", GoogleLogin.as_view(), name="google_login"),
]
