from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.views.generic import DetailView, RedirectView, UpdateView, ListView

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

news_list_view = NewsListView.as_view()

class TagPostsDetailView(DetailView, LoginRequiredMixin):
    template_name = 'blog/tag.html'
    model = Tag
    slug_field = "slug"
    slug_url_kwarg = "slug"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['news'] = News.objects.filter(tags__name__in=self.object.name)
        return context

tagged_post = TagPostsDetailView.as_view()
