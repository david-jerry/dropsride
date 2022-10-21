import threading
from threading import Thread

from django.conf import settings
from django.utils.safestring import mark_safe
from django.core.mail import EmailMultiAlternatives
from allauth.account.adapter import DefaultAccountAdapter
from dropsride.companies.models import Company
from dropsride.utils.logger import LOGGER

class EmailThread(Thread):
    def __init__(self, subject, html_content, from_email, recipient_list):
        self.subject = subject
        self.recipient_list = recipient_list
        self.from_email = from_email if from_email != "" else settings.DEFAULT_FROM_EMAIL
        self.html_content = html_content
        Thread.__init__(self)

    def run (self):
        msg = EmailMultiAlternatives(self.subject, self.html_content, self.from_email, self.recipient_list)
        msg.attach_alternative(mark_safe(self.html_content), "text/html")
        msg.content_subtype = "html"
        msg.send()

def send_html_mail(subject, html_content, from_email, recipient_list):
    EmailThread(subject, html_content, from_email, recipient_list).start()




class AccountEmails(threading.Thread, DefaultAccountAdapter):
    def __init__(self, template_prefix, email, context):
        self.template_prefix = template_prefix
        self.email = email
        self.context = context
        threading.Thread.__init__(self)
        DefaultAccountAdapter.__init__(self)


    def run (self):
        DefaultAccountAdapter.send_mail(self, template_prefix=self.template_prefix, email=self.email, context=self.context)
        # msg.send()

def send_auth_email(template_prefix, email, context):
    AccountEmails(template_prefix, email, context).start()


from allauth import app_settings
from allauth.account.utils import complete_signup
class SignupThreading(Thread):

    # complete_signup(self.request, self.user, app_settings.EMAIL_VERIFICATION, self.get_success_url())
    def __init__(self, request, user, settings, success, object):
        self.request = request
        self.user = user
        self.settings = settings
        self.success = success
        self.object = object
        super().__init__(self)

    def run(self):
        complete_signup(self.request, self.user, self.settings, self.success)
        if self.object:
            if Company.objects.filter(user=self.user).exists():
                Company.objects.filter(user=self.user).update(company_name=self.object)
                LOGGER.info("[COMPANY SIGNUP VIEW] Company name has been added")

def signup_users(request, user, settings, success, object):
    SignupThreading(request, user, settings, success, object).start()

