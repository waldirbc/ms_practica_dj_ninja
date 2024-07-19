from django.contrib.auth.hashers import make_password
from django.shortcuts import render
from django.http import HttpResponse
import csv
from api_usuarios.models import Usuario


def carga_csv(request):
    template = "usuarios/template_carga.html"

    if request.method == "GET":
        return render(request, template)

    csv_file = request.FILES['csv_file']
    if not csv_file.name.endswith('.csv'):
        return HttpResponse("Por favor, carga un archivo CSV.")

    file_data = csv_file.read().decode("utf-8")
    lines = file_data.split("\n")

    for line in lines:
        fields = line.split(",")
        if len(fields) < 6:
            continue

        Usuario.objects.create(
            nombre=fields[0],
            apellido_paterno=fields[1],
            apellido_materno=fields[2],
            edad=fields[3],
            username=fields[4],
            password=make_password(fields[5])
        )

    return HttpResponse("Usuarios cargados exitosamente")

