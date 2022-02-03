from django.urls import path
from django.views.generic.base import TemplateView

from .views import registration


urlpatterns = [
    path('registration', registration, name='registration'),
    path('terms_of_service', TemplateView.as_view(template_name='terms_of_service.html'), name='terms_of_service'),
]
