# src/config.py

import os

LDAP_ADDRESS = os.getenv('LDAP_ADDRESS', '192.168.56.11') #Ingresa dirección ip del servidor, o su nombre de host si se cuenta con DNS
LDAP_USERNAME = os.getenv('LDAP_USERNAME', 'Administrator@pod3test.local') #El usuario Administrator es usado por fines de laboratorio, cambiar por uno con permisos necesarios. Agregando el dominio 
LDAP_PASSWORD = os.getenv('LDAP_PASSWORD', 'Cisco123')#Contraseña del usuario
