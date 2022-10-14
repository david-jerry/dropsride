import json
import asyncio

from config.authenticate import SessionCsrfExemotAuthentication

from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from django.http.response import HttpResponse, JsonResponse, HttpResponsePermanentRedirect
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages
from django.views.decorators.http import require_GET, require_POST, require_http_methods
from django.urls import reverse
from django.templatetags.static import static
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import CreateView, FormView
from config.forms import ContactForm

from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from webpush import send_user_notification, send_group_notification

from dropsride.utils.logger import LOGGER

User = get_user_model()


@require_GET
def signup(request):
    return render(request, "account/pre_signup.html")


class SupportCreateView(FormView):

    def get(self, request, *args, **kwargs):
        form = ContactForm()
        context = {'form':form}
        return render(request, 'pages/contact.html', context=context)

    def post(self, request, *args, **kwargs):
        if "__field_name__" in request.POST:
            return self.validate_field(request)

        form = ContactForm(data=request.POST)
        # context = {'form':form}
        if form.is_valid():
            # phone = form.cleaned_data['phone']
            # name = form.cleaned_data['name']
            self.send_mail(valid_data=form.cleaned_data)
            # send_mail(subject=f"{name} | {phone}", message=form.cleaned_data['message'], from_email=form.cleaned_data['email'], recipient_list=['support@dropsride.com'], fail_silently=False)
            return JsonResponse(status=201, data={"message":"Support Mail Successfully Sent"})
        # return render(request, 'pages/contact.html', context=context)
        return super().post(request, *args, **kwargs)

    def validate_field(self, request):
        field_name = request.POST.get("__field_name__")
        form = ContactForm(request.POST)
        form.is_valid()
        return JsonResponse(status=203, data={
            "errors": form.errors.get(field_name, []),
        })

    def send_mail(self, valid_data):
        LOGGER.info(valid_data['name'])
        send_mail(subject=f"SUPPORT MAIL [{valid_data['name'].title()}]", message=f"Mobile Line: {valid_data['phone']}\n\nMessage: {valid_data['message']}", from_email=valid_data['email'], recipient_list=['support@dropsride.com'], fail_silently=False)
        pass

support = SupportCreateView.as_view()

# def support(request):
#     form = ContactForm()
#     if request.method == 'POST':
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             LOGGER.info(form.cleaned_data)
#             pass
#         return render(request, 'pages/contact.html', context={'form':form})
#     return render(request, 'pages/contact.html', context={'form':form})


# @api_view(["POST"])
# @authentication_classes([SessionCsrfExemotAuthentication])
# @permission_classes([IsAuthenticated])
@require_POST
@csrf_exempt
def send_notification(request):
    # registration_id = request.data.get('registration_id')
    # if registration_id:
    #     device = WebPushDevice.objects.get(registration_id=registration_id)
    #     if device:
    #         device.send_message('[PUSH NOTIFICATION] Hello World')

    # return HttpResponse()
    try:
        data = json.loads(request.body.decode('utf-8'))
        # LOGGER.info(data)
    except ValueError:
        return HttpResponse(status=400)

    # Process the push data to match with the model


    try:
        head = data.pop("head")
        # reg = data.pop("registration_id")
        body = data.pop("body")
        group = data.pop("group")
        # LOGGER.info(f"Data: {head}\nbody: {body}\ngroup: {group}")
        # user_id = data['id']
        # user = get_object_or_404(User, id=user_id)
        # if 'head' not in data or 'body' not in data or 'group' not in data:
        #     return JsonResponse(status=400, data={'message':"Invalid request"})


        payload = {
            'head': "Testing",
            'body': body,
            'icon': static('vendors/images/favicon/favicon.png'),
            # add url if there is a link to visit from the push notification
            'url': request._current_scheme_host,
        }
        # LOGGER.info(f"Payload: {payload}")

        if group is None or group == "" and request.user.is_authenticated:
            send_user_notification(user=request.user, payload=payload, ttl=1000)
        else:
            send_group_notification(group_name=group, payload=payload, ttl=1500)
        return JsonResponse(status=200, data={'message':"Notification sent"})
    except TypeError:
        return JsonResponse(status=500, data={'message':"An Error occurred while sending notification"})



@require_http_methods(['GET'])
def offline_view(request):
    title = "Offline Page"
    description = "You currently have no network, so we are serving you this offline page showcasing our top rated podcasts to listen to for free"
    author = "Jeremiah E David (http://darkcodr.codes)"
    can_link = reverse("offline")
    twitter_handle = "@darkcodr_codes"
    template = "pages/offline.html"
    context = {
        'title': title,
        'description': description,
        'author': author,
        'can_link': can_link,
        'twitter_handle': twitter_handle,
        'offline': True
    }
    return render(request, template, context)

@require_http_methods(['GET'])
def service_worker(request):
    sw_path = settings.ROOT_DIR / "frontend/build" / "sw.js"
    response = HttpResponse(open(sw_path).read(), content_type='application/javascript')
    return response

@require_http_methods(['GET'])
def service_worker_map(request):
    sw_path = settings.ROOT_DIR / "frontend/build" / "sw.js.map"
    response = HttpResponse(open(sw_path).read(), content_type='application/javascript')
    return response


# class AnonymousWebPushDeviceViewSet(WebPushDeviceViewSet):
#     def perform_create(self, serializer):
#         # if not is_authenticated, can still work
#         serializer.save()
#         return super().perform_create(serializer)
