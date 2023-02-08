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

**Contenedores:** Un contenedor es un paquete que tiene una aplicación con los elementos necesarios para su ejecución. 
El contenedor se puede encender como una máquina virtual, sin embargo no cuenta con un sistema operativo completo sino solo con los elementos necesarios.
Su tiempo de ejecución es de pocos segundos y es posible que yo pueda utilizar muchos contenedores en una máquina virtual. 

**Máquinas virtuales:** 


### Servicios de cómputo bajo demanda donde podemos encontrar por ejemplo los siguientes: 

![a](https://github.com/datalytics-mejorcondatos/AZ900-Azure-Fundamentals/blob/Develop/Material/Imagenes/a.jfif)

Los servicios del ejemplo son Infraestructuras como Servicios (IaaS) o Plataformas como Servicios (PaaS). 

¿Cómo crear una máquina virtual?
Para profundizar en la creación de estos recursos, en específico de las máquinas virtuales es indispensable hacer una lectura de la siguiente sección: https://learn.microsoft.com/es-mx/training/modules/describe-core-architectural-components-of-azure/7-exercise-create-azure-resource

Lo principal que hay que saber es que Azure te pide cuatro cosas fundamentales en los recursos
•	Suscripción: La cuenta en la que se va a cargar el costo.
•	Grupo de recursos: Es una carpeta en la cual está el recurso que quieres usar, en esta carpeta puede haber muchos recursos, sin embargo, ningún recurso se puede repetir en otros grupos de recursos.
•	Nombre: Nombre para el recurso, en este caso un nombre para la máquina virtual 
•	Región: Área geográfica donde quieres que esté el recurso.


*Azure virtual Machines Scale sets:* Agrupa las máquinas virtuales para aumentarles el almacenamiento, la memoria para mejorar el rendimiento.
*Azure Batch:* Sirve para ejecutar tareas que necesitan un alto rendimiento como por ejemplo simulaciones, procesamiento de videos, transformación de datos, etc.

Existen una cantidad grande de recursos con distintas funcionalidades así que es recomendable hacer una exploración profunda a los recursos. De acuerdo a tu rol en la empresa, usarás diferentes recursos 



- ### Máquinas virtuales, recursos y conjuntos de disponibilidad

- ### Recursos para las máquinas virtuales

- ### Alojamiento de aplicaciones

- ### Redes virtuales

Todos los servicios que ofrece Azure respecto a las redes virtuales son Infraestructuras como Servicio. 

A continuación presentaremos algunos ejemplos dentro de estos recursos:

![b](https://github.com/datalytics-mejorcondatos/AZ900-Azure-Fundamentals/blob/Develop/Material/Imagenes/b.png)

*Azure virtual networks:* Permiten que los recursos de Azure se comuniquen entre sí.
*Azure VPN Gateway:* Es una red privada virtual que mantiene la seguridad de la información almacenada en los recursos de Azure.
*Azure Application* Distribuye equitativamente las cargas de ejecución al asignar tareas.  

De nuevo, este es solo un ejemplo de este tipo de recursos pero se deja al lector inspeccionar los demás servicio de redes virtuales. 

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

