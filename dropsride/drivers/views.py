from django.shortcuts import render
from django.contrib.auth import get_user_model
from config.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.views.generic import DetailView, RedirectView, UpdateView, CreateView, ListView

User = get_user_model()

# Create your views here.
