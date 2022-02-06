from django.urls import path
from django.views.generic.base import TemplateView

from .views import registration, Login, Logout, Profile, ProfileChangeView

app_name = 'accounts_app'

urlpatterns = [
    path('registration', registration, name='registration'),
    path('terms_of_service', TemplateView.as_view(template_name='terms_of_service.html'), name='terms_of_service'),
    path('login', Login.as_view(), name='login'),
    path('logout', Logout.as_view(), name='logout'),
    path('profile/<int:pk>', Profile.as_view(), name='profile'),
    path('profile_change/<int:pk>', ProfileChangeView.as_view(), name='profile_change'),
]
