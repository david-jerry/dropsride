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

from .models import News
from .forms import NewsForm

from taggit.models import Tag

User = get_user_model()

# Create your views here.
class NewsListView(ListView):
    model = News
    template_name = "blog/list.html"
    context_object_name = "objects"
    page_kwarg = 'page'
    paginate_by = 20
    allow_empty = True
    queryset = News.objects.published()

list_view = NewsListView.as_view()

class NewsDetailView(DetailView):
    template_name = 'blog/detail.html'
    model = News
    slug_field = "slug"
    slug_url_kwarg = "slug"


detail_view = NewsDetailView.as_view()


class NewsCreateView(FormView, StaffRequiredMixin):
    model = News
    template_name = "blog/create.html"
    form_class = NewsForm

    def post(self, request, *args, **kwargs):

        if "__field_name__" in request.POST:
            return self.validate_field(request)

        form = NewsForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form = form.save(commit=False)
            form.author = request.user
            form.save()
            return JsonResponse(status=201, data={"message":"You have successfully created a new Career Opening", "title":"New Career Opening"})
        else:
            return JsonResponse(status=400, data={"message":"Invalid form details", "title":"Form Validation Error"})


    def validate_field(self, request):
        field_name = request.POST.get("__field_name__")
        form = NewsForm(request.POST, request.FILES)
        form.is_valid()
        return JsonResponse(status=203, data={
            "errors": form.errors.get(field_name, []),
        })

create_view = NewsCreateView.as_view()

class NewsUpdateView(UpdateView, StaffRequiredMixin):
    model = News
    template_name = "blog/update.html"
    form_class = NewsForm

    def post(self, request, *args, **kwargs):

        if "__field_name__" in request.POST:
            return self.validate_field(request)

        form = NewsForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return JsonResponse(status=201, data={"message":"You have successfully created a new Career Opening", "title":"New Career Opening"})
        else:
            return JsonResponse(status=400, data={"message":"Invalid form details", "title":"Form Validation Error"})


    def validate_field(self, request):
        field_name = request.POST.get("__field_name__")
        form = NewsForm(request.POST, request.FILES)
        form.is_valid()
        return JsonResponse(status=203, data={
            "errors": form.errors.get(field_name, []),
        })

update_view = NewsUpdateView.as_view()


class BlogDeleteView(DeleteView, StaffRequiredMixin):
    model = News
    template_name = 'blog/delete.html'
    slug_field = "slug"
    slug_url_kwarg = "slug"
    success_url = 'news:list'

delete_view = BlogDeleteView.as_view()
