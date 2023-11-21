from django.contrib import admin
from django.urls import path
from .views import BissextileYear
from .views import bissextile_range
from .views import endpoint_archives

urlpatterns = [
    path('is-bissextile', BissextileYear.as_view(), name='is-bissextile'),
    path('is-bissextile-range', bissextile_range, name='is-bissextile-range'),
    path('historique', endpoint_archives, name='historique'),
    ]
