from django.urls import path
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns
from .views import api_root, PropietarioList, PropietarioDetail, PredioList, PredioDetail

urlpatterns=[
  path('', api_root),
  path('propietarios/', PropietarioList.as_view(), name='propietario-list'),
  path('propietarios/<int:pk>/', PropietarioDetail.as_view(), name='propietario-detail'),
  path('predios/', PredioList.as_view(), name='predio-list'),
  path('predios/<int:pk>/', PredioDetail.as_view(), name='predio-detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)