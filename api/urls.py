from django.urls import path
from .views import PropietarioView, PredioView

urlpatterns=[
  path('propietarios/', PropietarioView.as_view(), name='propietarios_list'),
  path('propietarios/<int:id>', PropietarioView.as_view(), name='propietarios_process'),
  path('predios/', PredioView.as_view(), name='predios_list'),
  path('predios/<int:id>', PredioView.as_view(), name='predios_process'),
]