import json
from django.http.response import JsonResponse
from django.urls.base import clear_script_prefix
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from .models import Propietario, Predio

# Create your views here.

# Vista de Propietario

class PropietarioView(View):

  @method_decorator(csrf_exempt)
  def dispatch(self, request, *args, **kwargs):
      return super().dispatch(request, *args, **kwargs)

  def get(self, request, id=0):
    if(id>0):
      propietarios=list(Propietario.objects.filter(id=id).values())

      if len(propietarios)>0:
        propietario=propietarios[0]
        datos={'message': "Success", 'propietario': propietario}

      else:
        datos={'message': "Propietario not found..."}

      return JsonResponse(datos)

    else:
      propietarios=list(Propietario.objects.values())

      if len(propietarios)>0:
        datos={'message': "Success", 'propietarios': propietarios}
        
      else:
        datos={'message': "Propietarios not found..."}

      return JsonResponse(datos)

  def post(self, request):
    jd=json.loads(request.body)
    Propietario.objects.create(name=jd['name'], identificacion=jd['identificacion'])
    datos={'message': 'Success'}

    return JsonResponse(datos)

  def put(self, request, id):
    jd=json.loads(request.body)
    propietarios=list(Propietario.objects.filter(id=id).values())

    if len(propietarios)>0:
      propietario=Propietario.objects.get(id=id)
      propietario.name=jd['name']
      propietario.identificacion=jd['identificacion']
      propietario.save()
      datos={'message': 'Success'}

    else:
        datos={'message': "Propietario not found..."}

    return JsonResponse(datos)

  def delete(self, request, id):
    propietarios = list(Propietario.objects.filter(id=id).values())

    if len(propietarios)>0:
      Propietario.objects.filter(id=id).delete()
      datos={'message': 'Success'}
    
    else:
      datos={'message': "Propietario not found..."}

    return JsonResponse(datos)

# Vista de Predio

class PredioView(View):

  @method_decorator(csrf_exempt)
  def dispatch(self, request, *args, **kwargs):
      return super().dispatch(request, *args, **kwargs)

  def get(self, request, id=0):
    if(id>0):
      predios=list(Predio.objects.filter(id=id).values())

      if len(predios)>0:
        predio=predios[0]
        datos={'message': "Success", 'predio': predio}

      else:
        datos={'message': "Predio not found..."}

      return JsonResponse(datos)

    else:
      predios=list(Predio.objects.values())

      if len(predios)>0:
        datos={'message': "Success", 'predios': predios}
        
      else:
        datos={'message': "Predios not found..."}

      return JsonResponse(datos)

  def post(self, request):
    jd=json.loads(request.body)
    Predio.objects.create(name=jd['name'], predio=jd['predio'], matricula_inmobiliaria=jd['matricula_inmobiliaria'], cedula_catastral=jd['cedula_catastral'], propietarios=jd['propietarios'])
    datos={'message': 'Success'}

    return JsonResponse(datos)

  def put(self, request, id):
    jd=json.loads(request.body)
    predios=list(Predio.objects.filter(id=id).values())

    if len(predios)>0:
      predio=Predio.objects.get(id=id)
      predio.name=jd['name']
      predio.predio=jd['predio']
      predio.matricula_inmobiliaria=jd['matricula_inmobiliaria']
      predio.cedula_catastral=jd['cedula_catastral']
      predio.propietarios=jd['propietarios']
      predio.save()
      datos={'message': 'Success'}

    else:
        datos={'message': "Predio not found..."}

    return JsonResponse(datos)

  def delete(self, request, id):
    predios = list(Predio.objects.filter(id=id).values())

    if len(predios)>0:
      Predio.objects.filter(id=id).delete()
      datos={'message': 'Success'}
    
    else:
      datos={'message': "Predio not found..."}

    return JsonResponse(datos)