from rest_framework.authentication import SessionAuthentication

class SessionCsrfExemotAuthentication(SessionAuthentication):
    def enforce_csrf(self, request):
        pass
