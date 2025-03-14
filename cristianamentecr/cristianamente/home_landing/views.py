from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.


class HomeLandingPage(TemplateView):
    """Home/Landing page."""
    template_name = "home_landing.html"
