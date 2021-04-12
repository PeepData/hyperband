# hyperband
![python_version](https://img.shields.io/badge/python-3.8-blue)

Breve descripción acerca del proyecto.

## Installation
Listar las dependencias y requerimentos para poder utilizar el cli.

1-Instalar las dependencias.

```sh
pip3 install -r requirements.txt
pip3 install -e .
```

2-Configurar las variables de entorno.

```sh
MYSQL_USER=<user>
MYSQL_PASSWORD=<password>
MYSQL_HOST=<host>
MYSQL_PORT=<port>
MYSQL_DATABASE=<PYTHON_BI_{env}>
```
Para mis información sobre estas credenciales ingresar a este [wiki](https://agea.atlassian.net/wiki/spaces/BIGAA/pages/252707452/Herramientas).


## Usage

Indicar como debe ejecutarse. Por ejemplo el proyecto debe ser utilizado con el siguiente comando:

```sh
hyperband run <arg1> <arg2>
```

Para más información:

```sh
hyperband --help
```


## Running test
Para correr los tests existen dos opciones disponibles:

#### Tox
Por defecto `tox` tiene varios virtualenv disponibles para ejecutar. Para sólo ejecutar los tests se debe correr el siguiente comando:

```sh
tox -e test
```

#### Pytest
Se puede usar pytest directamente, se deben instalar las dependencias necesarias en el caso de que no lo estén y luego ejecutar el siguiente comando:

```sh
pytest
```


## Extra
Agregar más información sobre el proyecto en general. Por ejemplo la estructura de la data que se va a crear, el volumen de datos que puede mover, si tiene que tener permisos para llegar a una ip determinada, el motor de base de datos que se utilizará, etc.


## Schedule
Indicar cada cuanto deberá ejecutarse el proyecto.

| Comando                           | ¿Cómo y cuando?            |
| --------------------------------- | -------------------------- |
| hyperband run | Cada 8 HS                  |
