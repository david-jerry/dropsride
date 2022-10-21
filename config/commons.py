import threading
from threading import Thread

from django.conf import settings
from django.utils.safestring import mark_safe
from django.core.mail import EmailMultiAlternatives

class EmailThread(threading.Thread):
    def __init__(self, subject, html_content, from_email, recipient_list):
        self.subject = subject
        self.recipient_list = recipient_list
        self.from_email = from_email if from_email != "" else settings.DEFAULT_FROM_EMAIL
        self.html_content = html_content
        threading.Thread.__init__(self)

    def run (self):
        msg = EmailMultiAlternatives(self.subject, self.html_content, self.from_email, self.recipient_list)
        msg.attach_alternative(mark_safe(self.html_content), "text/html")
        msg.content_subtype = "html"
        msg.send()

def send_html_mail(subject, html_content, from_email, recipient_list):
    EmailThread(subject, html_content, from_email, recipient_list).start()
