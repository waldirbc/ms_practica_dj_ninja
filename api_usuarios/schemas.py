from ninja import ModelSchema

from .models import Usuario


class UsuarioSchemaCreate(ModelSchema):
    class Meta:
        model = Usuario
        fields = [
            "nombre",
            "apellido_paterno",
            "apellido_materno",
            "edad",
            "username",
            "password"
        ]


class UsuarioSchemaResponse(ModelSchema):
    class Meta:
        model = Usuario
        fields = [
            "nombre",
            "apellido_paterno",
            "apellido_materno",
            "edad",
            "username"
        ]