import asyncio
from dropsride.users.forms import UserLoginForm, UserSignupForm
import httpx

from allauth.account.views import SignupView, LoginView

from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.views.generic import DetailView, RedirectView, UpdateView, CreateView, ListView
from django.http import JsonResponse


from paystackapi.paystack import Paystack
from paystackapi.verification import Verification
from asgiref.sync import sync_to_async


from dropsride.drivers.models import Drivers
from dropsride.riders.models import Riders
from dropsride.users.models import UserNextOfKin


class UserSignupView(SignupView):
    def post(self, request, *args, **kwargs):
        if "__field_name__" in request.POST:
            return self.validate_field(request)

        # form = UserSignupForm(data=request.POST)
        # # context = {'form':form}
        # if form.is_valid():
        #     form.gave_consent = True
        #     form.save()
        #     # phone = form.cleaned_data['phone']
        #     # name = form.cleaned_data['name']
        #     # self.send_mail(valid_data=form.cleaned_data)
        #     # send_mail(subject=f"{name} | {phone}", message=form.cleaned_data['message'], from_email=form.cleaned_data['email'], recipient_list=['support@dropsride.com'], fail_silently=False)
        #     return JsonResponse(status=201, data={"message":f"Successfully signed up as {form.cleaned_data['username'].title()}"})
        # # return render(request, 'pages/contact.html', context=context)
        return super().post(request, *args, **kwargs)

    def validate_field(self, request):
        field_name = request.POST.get("__field_name__")
        form = UserSignupForm(request.POST)
        form.is_valid()
        return JsonResponse(status=203, data={
            "errors": form.errors.get(field_name, []),
        })

account_singup = UserSignupView.as_view()

class UserLoginView(LoginView):
    def post(self, request, *args, **kwargs):
        if "__field_name__" in request.POST:
            return self.validate_field(request)

        # form = UserLoginForm(data=request.POST)
        # # context = {'form':form}
        # if form.is_valid():
        #     try:
        #         form.login(request, redirect_url=self.get_success_url())
        #     except:
        #         self.form_valid(self, form=form)
        #     return JsonResponse(status=201, data={"message":f"Successfully signed up as {form.cleaned_data['username'].title()}"})
        return super().post(request, *args, **kwargs)

    def validate_field(self, request):
        field_name = request.POST.get("__field_name__")
        form = UserLoginForm(request.POST)
        form.is_valid()
        return JsonResponse(status=203, data={
            "errors": form.errors.get(field_name, []),
        })

account_login = UserLoginView.as_view()


User = get_user_model()
paystack = Paystack(secret_key=settings.PAYSTACK_TEST_SK)

class UserDetailView(LoginRequiredMixin, DetailView):

    model = User
    slug_field = "username"
    slug_url_kwarg = "username"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "User's Profile"
        return context


user_detail_view = UserDetailView.as_view()


class UserUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):

    model = User
    fields = ["first_name", "middle_name", "last_name", "country", "date_of_birth", "phone_number"]
    success_message = _("Information successfully updated")

    def get_success_url(self):
        assert (
            self.request.user.is_authenticated
        )  # for mypy to know that the user is authenticated
        return self.request.user.get_absolute_url()

    def get_object(self):
        return self.request.user

    def form_valid(self, form):
        return JsonResponse({"status":200, "message":"Updated User details successfully"})


user_update_view = UserUpdateView.as_view()



class UserRedirectView(LoginRequiredMixin, RedirectView):

    permanent = False

    def get_redirect_url(self):
        return reverse("users:detail", kwargs={"username": self.request.user.username})


user_redirect_view = UserRedirectView.as_view()



# ______________________________________________________________________ #
# function based views for user switches between driver and rider
# ______________________________________________________________________ #
@login_required
def driver_switch(request):
    if request.method == "POST":
        switched = request.POST.get("switched")
        if switched == "on":
            User.objects.filter(username=request.user.username).update(is_driver=True)
            # redirect(f"/users/driver/switch/?next=/{request.path}")
            return JsonResponse({"status":200, "message":"Switched to Driver"})
        else:
            User.objects.filter(username=request.user.username).update(is_driver=False)
            # redirect(f"/users/driver/switch/?next=/{request.path}")
            return JsonResponse({"status":200, "message":"Switched to Rider"})

# ______________________________________________________________________ #
# end of
# ______________________________________________________________________ #



@login_required
def add_next_of_kin(request):
    if request.method == "POST":
        name = request.POST.get("name")
        address = request.POST.get("address")
        image = request.POST.get("image")
        if (name, address, image) != "":
            UserNextOfKin.objects.create(user=request.user, name=name, address=address, image=image)
            return JsonResponse({"status":201, "message":"Successfully Added a New Next of Kin"})
        else:
            return JsonResponse({"status":400, "message":"Empty Field Error"})

# @login_required
# async def add_bank_account(request):
#     loop = asyncio.get_event_loop()
#     bvn = request.POST.get("bvn")
#     bank_code = request.POST.get("bank")
#     account_name = request.POST.get("name")
#     account_number = request.POST.get("number")
#     response = Verification.verify_account(account_number=account_number)


#     async_function = sync_to_async(response, thread_sensitive=False)
#     loop.create_task(async_function)
#     return JsonResponse({"status":201, "message":"Successfully Added a new account"})
    # async with httpx.AsyncClient() as client:
    #     data = {
    #         "bank_code":bank_code,
    #         "country_code": request.user.country.iso,
    #         "account_name": account_name,
    #         "account_number": account_number

    #     }
    #     headers = {"Authorization":settings.PAYSTACK_TEST_SK, "Content-Type":"application/json"}
    #     res = await client.get("https://api.paystack.co/bank/validate", headers=headers)


