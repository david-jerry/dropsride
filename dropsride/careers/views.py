from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.views import View
from django.views.generic.detail import SingleObjectMixin
from django.views.generic import DetailView, DeleteView, RedirectView, UpdateView, ListView, FormView
from django.http import JsonResponse

from config.mixins import StaffRequiredMixin
from dropsride.utils.logger import LOGGER

from .models import Careers, Applicants, Teams
from .forms import ApplicantsForm, CareersForm, DepartmentForm

from taggit.models import Tag

User = get_user_model()

# Create your views here.
class CareerListView(ListView):
    model = Careers
    template_name = "career/list.html"
    context_object_name = "objects"
    page_kwarg = 'page'
    paginate_by = 20
    allow_empty = True
    queryset = Careers.objects.published()

    def get_template_names(self):
        url = f"{self.request.scheme}://{self.request.META['HTTP_HOST']}{reverse('careers:list')}"
        home = f"{self.request.scheme}://{self.request.META['HTTP_HOST']}{reverse('home')}"
        # LOGGER.info(self.request.path == reverse('careers:list') and self.request.htmx)
        # LOGGER.info(self.request.META.get('HTTP_REFERER') == url)
        # LOGGER.info(self.request.path == reverse('careers:list'))
        if self.request.META.get('HTTP_REFERER') != url and self.request.htmx:
            LOGGER.info("serving from request without htmx 1")
            return 'career/list.html'
        elif self.request.META.get('HTTP_REFERER') != url and not self.request.htmx:
            LOGGER.info("serving from request without htmx 1")
            return 'career/list.html'
        elif self.request.path == reverse('careers:list') and self.request.htmx:
            LOGGER.info("serving from request with htmx 1")
            return 'snippets/career_list.html'
        # else:
        #     LOGGER.info("serving from request without htmx 1")
        #     return 'career/list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['counts'] = self.queryset.count()
        return context

list_view = CareerListView.as_view()

class CareerDetailView(DetailView):
    template_name = 'career/detail.html'
    model = Careers
    slug_field = "slug"
    slug_url_kwarg = "slug"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = ApplicantsForm()
        return context

class DepartmentDetailView(DetailView):
    template_name = 'career/department_detail.html'
    model = Teams
    slug_field = "slug"
    slug_url_kwarg = "slug"

department_detail_view = DepartmentDetailView.as_view()

class ApplicantDetailView(DetailView):
    template_name = 'career/applicant_detail.html'
    model = Applicants
    slug_field = "slug"
    slug_url_kwarg = "slug"

applicant_detail_view = ApplicantDetailView.as_view()


class ApplicantApplyView(FormView, SingleObjectMixin):
    template_name = 'career/detail.html'
    model = Careers
    form_class = ApplicantsForm
    slug_field = "slug"
    slug_url_kwarg = "slug"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        self.object = self.get_object()
        context['success_url'] = reverse('careers:detail', kwargs={'slug':self.object.slug})
        return

    def post(self, request, *args, **kwargs):

        if "__field_name__" in request.POST:
            return self.validate_field(request)

        form = ApplicantsForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            if not Applicants.objects.filter(position=self.get_object(), email=form.cleaned_data['email'], phone_number=form.cleaned_data['phone_number']):
                form = form.save(commit=False)
                form.position = self.get_object()
                form.save()
                return JsonResponse(status=201, data={"message":"You have successfully applied for this job role", "title":"Application Successful"})
            else:
                return JsonResponse(status=400, data={"message":"Sorry, You have already applied for this position", "title":"Application Failed or Invalid"})
        return JsonResponse(status=400, data={"message":"Sorry, You have applied for this job role", "title":"Application Successful"})


    def validate_field(self, request):
        field_name = request.POST.get("__field_name__")
        form = ApplicantsForm(request.POST, request.FILES)
        form.is_valid()
        return JsonResponse(status=203, data={
            "errors": form.errors.get(field_name, []),
        })


class CareerView(View):
    def get(self, request, *args, **kwargs):
        view = CareerDetailView.as_view()
        return view(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        view = ApplicantApplyView.as_view()
        return view(request, *args, **kwargs)

detail_view = CareerView.as_view()


class CareerCreateView(FormView, StaffRequiredMixin):
    model = Careers
    template_name = "career/create.html"
    form_class = CareersForm

    def post(self, request, *args, **kwargs):

        if "__field_name__" in request.POST:
            return self.validate_field(request)

        form = CareersForm(data=request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse(status=201, data={"message":"You have successfully created a new Career Opening", "title":"New Career Opening"})
        else:
            return JsonResponse(status=400, data={"message":"Invalid form details", "title":"Form Validation Error"})


    def validate_field(self, request):
        field_name = request.POST.get("__field_name__")
        form = CareersForm(request.POST)
        form.is_valid()
        return JsonResponse(status=203, data={
            "errors": form.errors.get(field_name, []),
        })

create_view = CareerCreateView.as_view()

class CreateDepartmentView(FormView, StaffRequiredMixin):
    model = Teams
    template_name = "career/department.html"
    form_class = DepartmentForm

    def post(self, request, *args, **kwargs):

        if "__field_name__" in request.POST:
            return self.validate_field(request)

        form = DepartmentForm(data=request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse(status=201, data={"message":"You have successfully created a new Career Department", "title":"New Career Department"})
        else:
            return JsonResponse(status=400, data={"message":"Invalid form details", "title":"Form Validation Error"})


    def validate_field(self, request):
        field_name = request.POST.get("__field_name__")
        form = DepartmentForm(request.POST)
        form.is_valid()
        return JsonResponse(status=203, data={
            "errors": form.errors.get(field_name, []),
        })

create_department_view = CreateDepartmentView.as_view()

class CareerDeleteView(DeleteView, StaffRequiredMixin):
    model = Careers
    template_name = 'career/delete.html'
    slug_field = "slug"
    slug_url_kwarg = "slug"
    success_url = 'careers:list'

delete_view = CareerDeleteView.as_view()


