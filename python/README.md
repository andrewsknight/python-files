# crear entornos de trabajo en python

## Paso 1

Para crear un entorno en python: 

        virtualenv backend

en este ejemplo el entorno se llama backend

## Paso 2: Activa el entorno de trabajo

        . backend/bin/activate
        cd backend

## Paso 3: Instalar depedencias

        # pip install nombreDeLaLibreria
        pip install Flask 

## Paso 4: Congelar las dependencias

Para generar las librerias que tiene cada proyecto y que otro programador pueda bajarse el programa e instalar las depedencias.

        pip freeze > requirements.txt