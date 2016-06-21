from django.shortcuts import render
from django.views.generic.base import TemplateView, CreateView
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class IndexView(TemplateView):
    template_name = "index.html"

class CreateUserView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = "/"
