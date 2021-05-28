# Script CPK, CP calculation for Effort machine cobot.

Script de cálculo y graficado de CP y CPK para cobot de máquina de esfuerzos desplegado en servidor local con pm2.

*Script CPK, CP calculation and plotting for Effort machine cobot deployed in local server with pm2.*


## Informacion
---

Esta aplicación recoge de la BBDD mysql en la 10.73.83.220 la información extraida de la máquina de fuezas con OPC client y calcula los cpks
El front end se puede acceder a traves de la URL: http://10.73.83.220/7qbs/

*This application collects from the mysql DB on 10.73.83.220 the information extracted from the power machine with OPC client and calculates the cpks
The front end can be accessed through the URL: http://10.73.83.220/7qbs/*
## Desarrollo
---

### Lenguajes:

* Python

### Desarrollada usando:

* PANDAS
* MATPLOTLIB
* mysql.connector

### BBDD:

* MySQL - 10.73.83.220@user.password - opcua_client_db


### Test de la API:

---

### Despliegue:


* Desplegada en:  `http://10.73.83.220/7qbs/`
* PM2: `10.73.82.219`

Para lanzarlo hay que abrir una consola y primero ejecutar el comando de abajo:

*To launch it you have to open a console and first execute the command below*

`PM2 ls`

Asi vemos si hay algun servicio ejecutandose.

*So we see if there is any service running*

después lanzar:

*then launch:*

`PM2 start setup.py --name CPK --interpreter py`

`pm2 startup`

`pm2 save`

### Repositorios:

* Front end 
* Back end 

## Licencia
---
ISRI
## Organización
---
### Empresa ISRINGHAUSEN: 

ISRINGHAUSEN es una empresa con más de 50 años de experiencia en la fabricación de asientos para vehículos industriales. A día de hoy es suministrador de muchas de las principales marcas de automoción internacional.

*ISRINGHAUSEN is a company with more than 50 years of experience in the manufacture of seats for industrial vehicles. Today it is a supplier to many of the main international automotive brands.*