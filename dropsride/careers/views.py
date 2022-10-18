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
            form = form.save(commit=False)
            form.position = self.get_object()
            form.save()
            return JsonResponse(status=201, data={"message":"You have successfully applied for this job role", "title":"Application Successful"})
        else:
            return JsonResponse(status=400, data={"message":"Invalid form details", "title":"Form Validation Error"})


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

    def post(self, request, args, **kwargs):
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


