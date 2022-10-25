from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import include, path, re_path
from django.contrib.sitemaps.views import sitemap
from django.views import defaults as default_views
from django.views.generic import TemplateView

from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from rest_framework.authtoken.views import obtain_auth_token

from webpush.views import save_info

from dropsride.sitesettings.views import cities_view
from dropsride.users.views import sms_verification_link, verify_phone_number, account_login, account_singup as account_signup, driver_singup as driver_signup, company_singup as company_signup, confirm_email, password_set, password_reset, password_reset_from_key, password_change
from .views import offline_view, send_notification, service_worker, service_worker_map, support
from config.sitemaps import StaticViewSitemap

sitemaps = {
    "static": StaticViewSitemap,
}

urlpatterns = [
    path("", TemplateView.as_view(template_name="pages/home.html"), name="home"),
    path("business/", TemplateView.as_view(template_name="pages/business.html"), name="business"),
    path("cities/", view=cities_view, name="cities"),
    path("features/", TemplateView.as_view(template_name="pages/features.html"), name="features"),
    path("support/", support, name="support"),
    path("offline/", offline_view, name="offline"),
    path(
        "about/", TemplateView.as_view(template_name="pages/about.html"), name="about"
    ),

    # PWA Urls
    path("sw.js", service_worker, name="service_worker"),
    path("sw.js.map", service_worker_map, name="service_worker_map"),
    # path('webpush/save_information/', view=save_info, name="save_webpush_info"),



    # Django Admin, use {% url 'admin:index' %}
    path('jet/', include('jet.urls', 'jet')),  # Django JET URLS
    path('jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),  # Django JET dashboard URLS
    path('admin/', include('admin_honeypot.urls', 'admin_honeypot')),
    path(settings.ADMIN_URL, admin.site.urls),
    # path(settings.ADMIN_DOC_URL, include("django.contrib.admindocs.urls")),

    # User management
    path("users/", include("dropsride.users.urls", namespace="users")),
    path("admins/UcR9JPT074regleE15Xsb0gSZol4lDff/", include("dropsride.admins.urls", namespace="staff")),
    path("accounts/login/", account_login, name="account_login"),
    path("accounts/rider/signup/", account_signup, name="rider_signup"),
    path("accounts/driver/signup/", driver_signup, name="driver_signup"),
    path("accounts/company/signup/", company_signup, name="company_signup"),
    path('accounts/verify-phone/<code>/<user>', sms_verification_link, name="sms_verify"),
    re_path(
        r"^accounts/confirm-email/(?P<key>[-:\w]+)/$",
        confirm_email,
        name="account_confirm_email",
    ),
    path("accounts/password/set/", password_set, name="account_set_password"),
    path("accounts/password/reset/", password_reset, name="account_reset_password"),
    path("password/change/", password_change, name="account_change_password",),
    re_path(r"^accounts/password/reset/key/(?P<uidb36>[0-9A-Za-z]+)-(?P<key>.+)/$",password_reset_from_key,name="account_reset_password_from_key",),
    path("accounts/", include("allauth.urls")),

    # Your stuff: custom urls includes go here
    path("coupons/", include("dropsride.promocodes.urls", namespace="coupons")),
    path("news/", include("dropsride.blog.urls", namespace="news")),
    path("careers/", include("dropsride.careers.urls", namespace="careers")),

    # push notification links
    path("send-notification/", send_notification, name="send_notification"),
    # path('create-wp-subscription', AnonymousWebPushDeviceViewSet.as_view({'post': 'create'}),
    #      name='create-wp-subscription'),
    path('webpush/save_information/', view=save_info, name="save_webpush_info"),
    path('webpush/', include('webpush.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
if settings.DEBUG:
    # Static file serving when using Gunicorn + Uvicorn for local web socket development
    urlpatterns += staticfiles_urlpatterns()

# MISC URLS
urlpatterns += [
    path('tinymce/', include('tinymce.urls')),
    path('i18n/', include('django.conf.urls.i18n')),
    path("sitemap.xml/", sitemap, kwargs={"sitemaps": sitemaps}, name="sitemap"),
    path("robots.txt/", TemplateView.as_view(template_name="robots.txt", content_type="text/plain"), name="robots"),
]

# API URLS
urlpatterns += [
    # API base url
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
