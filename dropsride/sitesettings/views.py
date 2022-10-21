from django.shortcuts import render
from django.urls import reverse
from django.views.generic import DetailView, DeleteView, RedirectView, UpdateView, ListView, FormView
from django.http import JsonResponse

from dropsride.sitesettings.models import Localization

# Create your views here.
class LocalizationListView(ListView):
    model = Localization
    template_name = "blog/list.html"
    context_object_name = "objects"
    page_kwarg = 'page'
    paginate_by = 20
    allow_empty = True
    queryset = Localization.objects.filter(active=True)

    def get_template_names(self):
        url = f"{self.request.scheme}://{self.request.META['HTTP_HOST']}{reverse('cities')}"
        if self.request.META.get('HTTP_REFERER') != url and self.request.htmx:
            return 'pages/cities.html'
        elif self.request.META.get('HTTP_REFERER') != url and not self.request.htmx:
            return 'pages/cities.html'
        elif self.request.path == reverse('careers:list') and self.request.htmx:
            return 'snippets/cities_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['counts'] = self.queryset.count()
        return context

cities_view = LocalizationListView.as_view()
