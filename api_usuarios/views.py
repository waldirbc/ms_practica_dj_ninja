from django.contrib.auth.hashers import make_password
from django.shortcuts import get_object_or_404
from ninja import Router
from ninja.errors import HttpError

from .models import Usuario
from .schemas import UsuarioSchemaResponse, UsuarioSchemaCreate

api = Router()


@api.get("/usuarios", response=list[UsuarioSchemaResponse])
def get_usuarios(request):
    return list(Usuario.objects.all())


@api.get("/usuarios/{username}", response=UsuarioSchemaResponse)
def get_usuario(request, username: str):
    return get_object_or_404(Usuario, username=username)


@api.post("/usuarios", response={201: UsuarioSchemaResponse, 400: dict})
def create_usuario(request, payload: UsuarioSchemaCreate):
    if Usuario.objects.filter(username=payload.username).exists():
        raise HttpError(400, "Username already exists")
    usuario_data = payload.dict()
    usuario_data['password'] = make_password(usuario_data['password'])
    usuario = Usuario.objects.create(**usuario_data)
    return 201, usuario


@api.put("/usuarios/{username}", response=UsuarioSchemaResponse)
def update_usuario(request, username: str, payload: UsuarioSchemaCreate):
    usuario = get_object_or_404(Usuario, username=username)
    if payload.username != username and Usuario.objects.filter(username=payload.username).exists():
        raise HttpError(400, "Username already exists")
    usuario.nombre = payload.nombre
    usuario.apellido_paterno = payload.apellido_paterno
    usuario.apellido_materno = payload.apellido_materno
    usuario.edad = payload.edad
    usuario.username = payload.username
    usuario.password = make_password(payload.password)
    usuario.save()
    return usuario


@api.delete("/usuarios/{username}", response={204: None, 404: dict})
def delete_usuario(request, username: str):
    usuario = get_object_or_404(Usuario, username=username)
    usuario.delete()
    return 204, None
