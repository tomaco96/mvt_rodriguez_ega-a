from django.http import HttpResponse
from django.shortcuts import render

from app_coder.models import Familiar
def familia(self, nombre, edad, cumpleaños):
    familia =Familiar(nombre=nombre, edad=edad, cumpleaños=cumpleaños)
    familia.save()
    return HttpResponse(f"""<p>{familia.nombre} - {familia.edad} - {familia.cumpleaños}""")
def lista_familia(self):
    lista= Familiar.objects.all()
    return render(self, "template1.html", {"lista_familia": lista})
# Create your views here.
