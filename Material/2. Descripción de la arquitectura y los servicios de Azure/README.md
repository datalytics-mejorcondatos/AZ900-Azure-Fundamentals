# Arquitectura y servicios de Azure


## 1. Componentes arquitectónicos de Azure

- ### Regiones
Una región es un área geográfica donde Azure, o en general un proveedor de servicios en la nube tiene al menos un centro de datos físico.
A continuación, los puntos azules son los centros de datos físicos con los que cuenta Azure al rededor del mundo.

![6](https://github.com/datalytics-mejorcondatos/AZ900-Azure-Fundamentals/blob/Develop/Material/Imagenes/6.png)

Gracias a estos centros de datos distribuidos estratégicamente, se garantiza que los servicios de Azure de una región ofrezcan el mejor rendimiento y seguridad.
Aunque algunos servicios de las máquinas virtuales solo están disponibles en determinadas regiones, como tipos de almacenamiento o tamaños de maquinas virtuales específicos. También hay algunos servicios globales de Azure que no requieren que seleccione una región concreta.

Si quieres tener una exploración de estas regiones puedes ingresar a la página oficial: https://infrastructuremap.microsoft.com/

- ### Zonas de disponibilidad

 Las zonas de disponibilidad son centros de datos separados físicamente dentro de una región de Azure. Las zonas de disponibilidad están conectadas a través de redes de fibra óptica de alta velocidad privadas como se muestra en la figura:
 
 ![7](https://github.com/datalytics-mejorcondatos/AZ900-Azure-Fundamentals/blob/Develop/Material/Imagenes/7.png)

Estas zonas de disponibilidad tienen un propósito y es proteger la información que un centro de datos tiene en caso de un desastre natural que afecte una zona, respaldando y haciendo una copia en otra zona de disponibilidad.
También hay otros tipos de usos entre zonas de disponibilidad como darle mayor rendimiento a un recurso. 
Las zonas de disponibilidad son principalmente para las máquinas virtuales, los discos administrados, los equilibradores de carga y las bases de datos SQL.  

Los servicios de Azure que admiten zonas de disponibilidad se dividen en tres categorías: 

* **Servicios de zona:** ancle el recurso a una zona específica (por ejemplo, máquinas virtuales, discos administrados, direcciones IP). 
* **Servicios de redundancia de zona:** la plataforma se replica automáticamente entre zonas (por ejemplo, almacenamiento con redundancia de zona, SQL Database). 
* **Servicios no regionales:** los servicios siempre están disponibles en las ubicaciones geográficas de Azure y son resistentes a las interrupciones de toda la zona, así como a las de toda la región. 

Incluso con la resistencia adicional que proporcionan las zonas de disponibilidad, es posible que un evento pueda ser tan grande que afecte a varias zonas de disponibilidad en una sola región. Para proporcionar una mayor resistencia, Azure tiene pares de regiones. 


- ### Pares de regiones

Una región se empareja con otra de la misma zona geográfica (debe estar a mínimo 500 km de distancia) para replicar recursos con el fin de respaldar la región y la información que maneja de eventos que puedan interrumpir el funcionamiento normal de la región y las zonas de disponibilidad.


- ###  Recursos y grupos de recursos

![8](https://github.com/datalytics-mejorcondatos/AZ900-Azure-Fundamentals/blob/Develop/Material/Imagenes/8.png)

#### Características 
* Alta disponibilidad: Los servicios de nube están habilitados independientemente de si ocurre un evento que ponga en peligro una región de Azure. 
* Tolerancia a fallos: Se aprende del error y sse trabaja sobre el mismo para la mejora. Siempre va a estar disponible la información.
* Agilidad: La creación de distintas tareas es rápida dado que los recursos que se tienen ahí minimizan la complejidad.
* *Elasticidad:* Un recurso se autoescala para cubrir las necesidades que se presenten. Esta característica se produce de forma automática. Para más información sobre esta defición, ingresar a https://azure.microsoft.com/en-gb/resources/cloud-computing-dictionary/what-is-elastic-computing/

- ### Suscripciones

- ### Grupos de gestión

- ### Jerarquías 

## 2. Servicios informáticos y de red de Azure

- ### Tipos de computación, máquinas virtuales y contenedores

- ### Máquinas virtuales, recursos y conjuntos de disponibilidad

- ### Recursos para las máquinas virtuales

- ### Alojamiento de aplicaciones

- ### Redes virtuales

- ### Puntos finales públicos y privados


## 3. Servicios de almacenamiento

- ### Comparación de servicios de almacenamiento

- ### Niveles de almacenamiento

- ### Opciones de redundancia

- ### Cuenta de almacenamiento y tipos de almacenamiento

- ### Movimientos de archivos

- ### Migración

## 4. Identidad, acceso y seguridad de Azure

- ### Servicios de directorio de Azure

- ### Métodos de autenticación

- ### Identidades externas y acceso de invitados

- ### Acceso condicional

- ### Control de acceso

- ### Confianza sero

- ### Modelo de defensa en profundidad

- ### Microsoft Defender for Cloud

