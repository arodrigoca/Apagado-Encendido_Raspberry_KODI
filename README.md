# Apagado-Encendido_Raspberry_KODI
Pequeño Script para que al pulsar un botón seamos capaces de apagar la Raspberry de manera segura y con el mismo se encienda.

Primero deberemos de instalar todos los paquetes necesarios de python y los módulos que no vienen preinstalados con Kodi.

-- sudo apt-get install python-dev

Las versiones de GPIO pueden ir actualizandose con el tiempo

-- sudo wget https://pypi.python.org/packages/e2/58/6e1b775606da6439fa3fd1550e7f714ac62aa75e162eed29dbec684ecb3e/RPi.GPIO-0.6.3.tar.gz

-- tar zxf RPi.GPIO-0.6.3.tar.gz 

Dentro de la carpeta descomprimida 

-- sudo python setup.py install 

volvemos a Home
En esta carpeta es donde guardaremos nuestro script

-- mkdir scripts (o como queramos llamar a esta carpeta)

Para ejecutar el script 

-- sudo python  shutdown.py

Y listo!!! Para apagar la Raspberry simplemente tendremos que presionar brevemente el pulsador

Configuración del script para que se ejecute cada vez que se inicie la Raspberry.
--------------------------------------------------------------------------------
--sudo crontab -e

Introducimos la siguiente linea al final del crontab:

--@reboot sudo python /home/pi/"path_del_archivo"/shutdown.py

Listo!!!


