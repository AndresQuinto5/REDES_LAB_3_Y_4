# REDES_LAB_3_Y_4
# Laboratorio 3 - Algoritmos de enrutamiento 

## Antecedentes
Conociendo a dónde enviar los mensajes para cualquier router se vuelve trivial el envío de mensajes. Únicamente es necesario conocer el destino final y se reenvía al vecino que puede proveer la mejor ruta al destino. Toda esa información es almacenada en las tablas de enrutamiento.
No obstante, con el dinamismo con el que se espera que pueda funcionar el Internet es necesario que dichas tablas puedan actualizarse y acomodarse a cambios en la infraestructura. Los algoritmos con los que se actualizan estas tablas son conocidos como algoritmos de enrutamiento.

## Objetivos
- Conocer los algoritmos de enrutamiento utilizados en las implementaciones actuales de Internet.
- Comprender cómo funcionan las tablas de enrutamiento.

## Algoritmos a implementar
-  Flooding
-  Distance Vector Routing
-  Link State Routing

## Requerimientos de instalacion
Las herramientas usadas para el desarrollo y uso del programa fueron:
```sh
Python 3.7+ #No probamos en otra version de python, solo en 3.7.0, asi que prueben con esta version para que sea estable
Slixmpp 1.7.1
aioconsole 0.3.2
aiodns 3.0.0
cffi 1.14.6
cycler 0.10.0
kiwisolver 1.3.2
matplotlib 3.4.3
networkx 2.6.2
numpy 1.21.2
Pillow 8.3.1
pkg_resources 0.0.0
pyasn1 0.4.8
pyasn1-modules 0.2.8
pycares 4.0.0
pycparser 2.20
pyparsing 2.4.7
python-dateutil 2.8.2
PyYAML 5.4.1
six 1.16.0
```
Puedes instalarlas usando el siguiente comando:
```sh
pip install -r requirements.txt 
```

### Nota
puede que la libreria pkg_resources de problemas, es por eso que la tenemos comentada, si a ti no te da problema porfavor instalarla.

Para ejecutar 
```sh
py main.py
```
