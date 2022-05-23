from django.http import HttpResponse
from django.shortcuts import render
from app_mvt.models import familia
from django.template import loader
# Create your views here.


#listado de familia
def flia(request):
    flia=familia.objects.all()
    datos={"Datos" : flia}
    return render(request,"lista_flia.html",datos)

#Cargar un familiar
def alta_flia(request,nombre,fecha,edad,parentesco):
    familiar= familia(nombre=nombre, nacimiento=fecha,edad=edad,parentesco=parentesco)
    familiar.save()
    texto= f"Se guardo en la BD al familiar: {familiar.nombre} "
    return HttpResponse(texto)