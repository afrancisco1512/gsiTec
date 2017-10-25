from django.shortcuts import render, HttpResponse
from models import Ticket

# Create your views here.

def home(request):
    if request.user == 'AnonymousUser':
         pass
    else:
        return render(request, 'index.html')




def CrearTicket(request):
    if request.method == "POST":
        dato = Ticket(
            nombre = request.POST['name'],
            email = request.POST['email'],
            titulo = request.POST['titulo'],
            mensage = request.POST['mensaje']
            prioridad = request.POST['prioridad'],
            servicio = request.POST['servicio'],
            #Archivo = request.POST['Archivo']
            )
        dato.save()
        return render(request, 'index.html')
