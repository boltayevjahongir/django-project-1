from django.urls import path
from .views import home

urlpatterns = [
    path('', home, name='home'),
    path('about/', home, name='about')
]