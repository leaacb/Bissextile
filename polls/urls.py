from django.urls import path

from .views import BissextileYear, BissextileRangeYear
from .views import endpoint_archives

urlpatterns = [
    path('is-bissextile', BissextileYear.as_view(), name='is-bissextile'),
    path('is-bissextile-range', BissextileRangeYear.as_view(), name='is-bissextile-range'),
    path('historique', endpoint_archives, name='historique'),
    ]
