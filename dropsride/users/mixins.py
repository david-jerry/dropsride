from django.contrib.auth.mixins import AccessMixin
from django.contrib.auth.views import redirect_to_login
from django.core.exceptions import PermissionDenied
from django.urls import reverse_lazy


class LoginRequiredMixin(AccessMixin):
    """Verify that the current user is authenticated and redirect to login page if not."""

    login_url = reverse_lazy("account_login")

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect_to_login(
                request.get_full_path(),
                self.get_login_url(),
                self.get_redirect_field_name(),
            )
        return super().dispatch(request, *args, **kwargs)


class StaffRequiredMixin(AccessMixin):
    """Verify that the current user is a staff member and redirect to login page if not."""

    login_url = reverse_lazy("account_login")

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect_to_login(
                request.get_full_path(),
                self.get_login_url(),
                self.get_redirect_field_name(),
            )
        elif not request.user.is_staff:
            return PermissionDenied
        return super().dispatch(request, *args, **kwargs)
