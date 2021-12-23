from rest_framework import generics, mixins
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from .models import Propietario, Predio
from .serializers import PropietarioSerializer, PredioSerializer

@api_view(['GET'])
def api_root(request, format=None):
  return Response({
    'propietarios': reverse('propietario-list', request=request, format=format),
    'predios': reverse('predio-list', request=request, format=format)
  })

class PropietarioList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
  queryset = Propietario.objects.all()
  serializer_class = PropietarioSerializer

  def get(self, request, *args, **kwargs):
    return self.list(request, *args, **kwargs)

  def post(self, request, *args, **kwargs):
    return self.create(request, *args, **kwargs)

class PropietarioDetail(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
  queryset = Propietario.objects.all()
  serializer_class = PropietarioSerializer

  def get(self, request, *args, **kwargs):
    return self.retrieve(request, *args, **kwargs)

  def put(self, request, *args, **kwargs):
    return self.update(request, *args, **kwargs)

  def delete(self, request, *args, **kwargs):
    return self.destroy(request, *args, **kwargs)

class PredioList(generics.ListAPIView):
  queryset = Predio.objects.all()
  serializer_class = PredioSerializer
  filter_backends = [DjangoFilterBackend, SearchFilter]
  filterset_fields = ['propietarios__name', 'propietarios__identificacion', 'cedula_catastral', 'direccion', 'name']
  # search_fields = ['$propietarios__name', '$propietarios__identificacion', '$cedula_catastral', '$direccion', '$name', 'type_predio']

class PredioCreate(mixins.CreateModelMixin, generics.GenericAPIView):
  queryset = Predio.objects.all()
  serializer_class = PredioSerializer

  def post(self, request, *args, **kwargs):
    return self.create(request, *args, **kwargs)

class PredioDetail(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
  queryset = Predio.objects.all()
  serializer_class = PredioSerializer

  def get(self, request, *args, **kwargs):
    return self.retrieve(request, *args, **kwargs)

  def put(self, request, *args, **kwargs):
    return self.update(request, *args, **kwargs)

  def delete(self, request, *args, **kwargs):
    return self.destroy(request, *args, **kwargs)
