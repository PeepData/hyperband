# Hyperband
![python_version](https://img.shields.io/badge/python-3.8-blue)

Breve ejemplo acerca Hyperband utilizando [Xgboost](https://xgboost.readthedocs.io/en/latest/). La versión original de la implementación de la clase [Hyperband](https://arxiv.org/abs/1603.06560) se encuentra en este [repositorio](https://github.com/zygmuntz/hyperband).

El template del proyecto está disponible en el siguiente [LINK](https://github.com/PeepData/cookiecutter_python_cli).

## Installation

### Utilizando el requirements.txt

Instalar las dependencias:

```sh
pip3 install -r requirements.txt
pip3 install -e .
```

Utilizar pip en el caso de utilizar Windows.


### Utilizando Docker

Para facilitar el uso, hay disponible un Makefile. Para utilizar ejecutar los siguientes comandos para iniciar el ambiente:


Para buildear contenedor:
```sh
make build
```


## Usage

El proyecto puede correrse simplemente utilizando el siguiente comando:

```sh
hyperband run
```

Para más información:

```sh
hyperband --help
```

Tambíen se puede ejecutar utilizando Docker. Una vez construida la imagen ejecutar los siguientes comando:

Para correr el contenedor:

```sh
make run
```

Para correr el proyecto:

```sh
make start
```


## Estructura del proyecto

* **/__ main __.py**: root del proyecto. Se encuentra la ejecución del método principal.
* **/service/hyperband.py**: implementación del algoritmo.
* **/service/xgboost.py**: declaración del espacio de búsqueda e instanciación del modelo.
* **/commons/helper.py**: funciones auxiliares para carga y transformación de datos, y evaluación del modelo.
* **/settings.py**: variables claves para el desarrollo de la hiperparametrización. En el caso de querer correr el proyecto con otros valores, modificar este archivo.

## Contacto
Cualquier comentario o dudas contactame a thepeepdata@gmail.com.
