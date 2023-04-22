import notifications.urls
from dj_rest_auth.views import PasswordResetConfirmView, PasswordResetView
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import include, path
from django.views import defaults as default_views
from django.views.generic import TemplateView
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from rest_framework.authtoken.views import obtain_auth_token
from webpush.views import save_info

from config.sitemaps import StaticViewSitemap
from dropsride.core.views import (  # service_worker_map,
    index_map,
    mark_read,
    offline_view,
    ref_home,
    save_cordinates,
    send_notification,
    send_user_push_notification,
    service_worker,
    support,
)
from dropsride.users.views import facebook_callback, google_callback

sitemaps = {
    "static": StaticViewSitemap,
}

urlpatterns = [
    path("", TemplateView.as_view(template_name="pages/home.html"), name="home"),
    path(
        "about/", TemplateView.as_view(template_name="pages/about.html"), name="about"
    ),
    path(
        "cards/verify/",
        TemplateView.as_view(template_name="pages/closePayment.html"),
        name="verify_payment",
    ),
    path("support/", support, name="support"),
    path(
        "features/",
        TemplateView.as_view(template_name="pages/features.html"),
        name="features",
    ),
    path("offline/", offline_view, name="offline"),
    # PWA Urls
    path("sw.js", service_worker, name="service_worker"),
    path("static/index.html", index_map, name="index_map"),
    # web push notificattions
    path("send-notification/", send_notification, name="send_notification"),
    path(
        "send-user-push-notification/",
        send_user_push_notification,
        name="send_user_push_notification",
    ),
    path("webpush/save_information/", view=save_info, name="save_webpush_info"),
    path("webpush/", include("webpush.urls")),
    # Django Admin, use {% url 'admin:index' %}
    path("jet/", include("jet.urls", "jet")),  # Django JET URLS
    path("jet/dashboard/", include("jet.dashboard.urls", "jet-dashboard")),
    path(settings.ADMIN_URL, admin.site.urls),
    path(settings.ADMIN_DOC_URL, include("django.contrib.admindocs.urls")),
    # User management
    path(
        "users/transactions/",
        include("dropsride.transactions.urls", namespace="transactions"),
    ),
    path("users/", include("dropsride.users.urls", namespace="users")),
    path("settings/", include("dropsride.settings.urls", namespace="settings")),
    path("trips/", include("dropsride.rides.urls", namespace="rides")),
    # social authentication callback urls for web only
    path("accounts/facebook/callback/", facebook_callback, name="facebook_callback"),
    path("accounts/google/callback/", google_callback, name="google_callback"),
    path("accounts/", include("allauth.urls")),
    # Your stuff: custom urls includes go here
    path("news/", include("dropsride.blog.urls", namespace="news")),
    path("careers/", include("dropsride.careers.urls", namespace="careers")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
if settings.DEBUG:
    # Static file serving when using Gunicorn + Uvicorn for local web socket development
    urlpatterns += staticfiles_urlpatterns()

# MISC URLS
urlpatterns += [
    path("select2/", include("django_select2.urls")),
    path("tinymce/", include("tinymce.urls")),
    path(
        "inbox/notifications/", include(notifications.urls, namespace="notifications")
    ),
    path("i18n/", include("django.conf.urls.i18n")),
    path("sitemap.xml/", sitemap, kwargs={"sitemaps": sitemaps}, name="sitemap"),
    path(
        "robots.txt/",
        TemplateView.as_view(template_name="robots.txt", content_type="text/plain"),
        name="robots",
    ),
]


# API URLS
urlpatterns += [
    # API base url
    path(
        "rest-auth/password/reset/confirm/<str:uidb64>/<str:token>/",
        TemplateView.as_view(template_name="account/password_reset_from_key.html"),
        name="password_reset_confirm",
    ),
    path("api/", include("config.api_router")),
    # DRF auth token
    path("auth-token/", obtain_auth_token),
    path("api/schema/", SpectacularAPIView.as_view(), name="api-schema"),
    path(
        "api/docs/",
        SpectacularSwaggerView.as_view(url_name="api-schema"),
        name="api-docs",
    ),
]

if settings.DEBUG:
    # This allows the error pages to be debugged during development, just visit
    # these url in browser to see how these error pages look like.
    urlpatterns += [
        path(
            "400/",
            default_views.bad_request,
            kwargs={"exception": Exception("Bad Request!")},
        ),
        path(
            "403/",
            default_views.permission_denied,
            kwargs={"exception": Exception("Permission Denied")},
        ),
        path(
            "404/",
            default_views.page_not_found,
            kwargs={"exception": Exception("Page not Found")},
        ),
        path("500/", default_views.server_error),
    ]
    if "debug_toolbar" in settings.INSTALLED_APPS:
        import debug_toolbar

        urlpatterns = [path("__debug__/", include(debug_toolbar.urls))] + urlpatterns


urlpatterns += [
    path("<int:id>/", mark_read, name="mark_read"),
    path("ref/<str:ref_number>/", ref_home, name="ref_home"),
    path("add-location/<lat>/<long>/", save_cordinates, name="save_cordinates"),
]
