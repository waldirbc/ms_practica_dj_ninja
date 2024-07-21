# Microservicio con Django Ninja

## Ejecutar el proyecto

Para ejecutar el proyecto, es necesario tener instalado `docker`.

```bash
docker build -t ms_practica_dj_ninja .
docker run -p 8002:8000 ms_practica_dj_ninja
```

## Consultar la API

Para consultar la API, se puede acceder a `http://localhost:8002/docs`.

## Ejemplo de consulta

Se adjunta json insomnia de pruebas en la carpeta `insomnia`.

## Carga masiva de datos

Para cargar masivamente datos, tiene que ingresar a la pagina: `http://localhost:8002/carga_csv/` 
y en el boton de examinar seleccionar el archivo csv que desea cargar. Y luego dar click en el boton de cargar.
