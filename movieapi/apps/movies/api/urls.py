from django.urls import path

from apps.movies.api.viewsets.general_views import MeasureUnitListAPIView,IndicatorListAPIView,CategoryProductListAPIView
from apps.movies.api.viewsets.product_views import (
    MovieListCreateAPIView,MovieRetrieveUpdateDestroyAPIView
)

urlpatterns = [
    path('measure_unit/', MeasureUnitListAPIView.as_view(), name = 'measure_unit'),
    path('indicator/', IndicatorListAPIView.as_view(), name = 'indicator'),
]
