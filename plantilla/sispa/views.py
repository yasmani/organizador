from django.shortcuts import render
from django.http import JsonResponse
from django.utils.timezone import now
from .models import AREA, SOLICITUD

# Create your views here.

def index(request):
    areas = AREA.objects.all()  # Obtener todas las áreas
    context = {
        'today': now(),
        'areas': areas
    }
    return render(request, "inicio.html", context)


def obtener_solicitudes(request):
    identificador = request.GET.get('identificador')
    solicitudes = SOLICITUD.objects.filter(id_rel=identificador).values('id_rel', 'solicitud')
    return JsonResponse(list(solicitudes), safe=False)


