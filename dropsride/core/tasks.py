from time import sleep

from django.core.mail import EmailMessage
from django.template import Context
from django.template.loader import get_template, render_to_string
from django.templatetags.static import static

from config import celery_app
from dropsride.utils.logger import LOGGER

logo = static("vendors/images/favicons/logo.png")


@celery_app.task()
def send_html_email(
    subject: str,
    template: str,
    from_email: str,
    context: dict,
    to_email: list,
    reply_to: str,
    attachment: str | None,
):
    """Sending Emails to a celery task que to improve performance

    Use:
        from config.celery_tasks import send_html_email
        send_html_email(subject, template, from_email, context={'key':'value'}, to_email=['email@address.com'], reply_to, attachment="quote.pdf")

    Args:
        subject (str): AN email subject
        template (str): template name from the templates folder to use for sending the email as HTML
        from_email (str): email address from usually a username tied to the verified domain on mailtrap
        context (dict): A dictionary to contain all context variables for the html template
        to_email (List[str]): A list of email addresses to send to
        reply_to (str): an email address to reply emails to
        attachment (str): an attachment file
    """
    body = render_to_string(template, context)

    mail = EmailMessage(
        subject=subject,
        body=body,
        from_email=from_email,
        to=to_email,
        reply_to=reply_to,
    )
    mail.content_subtype = "html"
    mail.attach("logo.png", logo, "image/png")
    # attach a file from the backend to be sent with teh email to a user via email
    if attachment is not None:
        mail.attach_file(attachment)
    mail.send()
