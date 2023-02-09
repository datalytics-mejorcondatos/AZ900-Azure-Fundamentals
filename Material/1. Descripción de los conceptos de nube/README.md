# Conceptos de nube

## 1. Computación en nube

- ### La nube
 ![1](https://github.com/datalytics-mejorcondatos/AZ900-Azure-Fundamentals/blob/Develop/Material/Imagenes/1.jpg)

Cuando hablamos de la nube como un concepto computacional, la manera más fácil de entender es pensando en esta como el computador de otra persona en el que voy a ejecutar distintas tareas. La ejecución de estas tareas se facilita por medio de servicios que me presta la nube a través de la conexión a internet.  

¿Qué servicios me puede prestar? Espacio de almacenamientos, uso de CPUs en centros de datos, etc.

### Centro de datos 
![2](https://github.com/datalytics-mejorcondatos/AZ900-Azure-Fundamentals/blob/Develop/Material/Imagenes/2.png)

El [centro de datos](https://infrastructuremap.microsoft.com/explore/datacenter) o datacenter es un término que de aquí en adelante será usado frecuentemente para referirse al espacio físico donde se encuentran los recursos necesarios de un proveedor de servicios tales como computadores, redes, sistemas de almacenamiento, etc. 


- ### Modelo basado en el consumo
![3](https://github.com/datalytics-mejorcondatos/AZ900-Azure-Fundamentals/blob/Develop/Material/Imagenes/3.jpg)

Antes de hablar del modelo basado en el consumo, es importante aclarar dos conceptos los cuales son:

***CAPEX** (Gastos de capital):* La compra de un espacio físico, servidores, dispositivos de matenimiento, gasto de luz, entre otros son los gastos de capital y esto consiste en adiquirir un producto (sea físico o no) y tenerlo disponible para mi empresa.

***OPEX** (Gastos de operación):* Es el dinero invertido en servicios a lo largo en el tiempo para el funcionamiento de mi empresa, tal como el alquiler del espacio físico donde voy a tener el centro de datos, alquiler de un vehículo para transportar mis servidores al momento de hacer mantenimiento o adquirir un servicio en la nube. Se puede traducir en el pago de un servicio que me presta alguien más. 

#### Ventajas del modelo basado en el consumo
1. No se paga por adelantado. 
2. No es necesario comprar infraestructuras costosas que muy posiblemente no serán utilizadas en su totalidad.
3. Se puede pagar para obtener más recursos cuando se necesiten y así mismo dejar de pagar cuando ya no se necesiten.

- ### Modelos de nube y usos
Existen tres tipos de nubes:

1. ***Nube pública:*** Es una nube que un proveedor crea, controla y mantiene donde cualquier persona que quiera comprar servicios en la nube puede acceder a estos recursos y usarlos, ya sea una empresa o un individuo. Esta nube se ofrece desde una conexión de internet público.

2. ***Nube privada:*** Esta nube es propia de una empresa y proporciona un control mayor en los servicios que esta utiliza. Una nube privada se puede hospedar desde el centro de datos físico de la empresa. Tiene mayores costos. 

3. ***Nube híbrida:*** Una nube híbrida es una mezcla entre nube pública y nube privada, que consta en incrementar la nube privada a través de la implementación de recursos de nube pública con el fin de solventar problemas como la alta demanda temporal de algunos servicios. La nube híbrida se puede usar para proporcionar más seguridad. 

También existen estas nubes:

**Nubes múltiples:** Varias nubes tienen dos (o más) proveedores de nube pública y administra los recursos y la seguridad en ambos entornos. 

**Azure Arc:** Es un conjunto de tecnologías que ayudan a administrar el entorno en la nube, tanto si se trata de una nube pública, una nube privada en el centro de datos, una configuración híbrida o incluso un entorno de varias nubes que se ejecuta en varios proveedores de la nube a la vez. 


- ### Responsabilidad compartida

**Proveedor de servicios en la nube:** El proveedor en este caso es quien presta los servicios de la nube, como por ejemplo Azure, AWS,Google Cloud, IBM Cloud, etc. 

**Consumidor:** Los consumidores de servicios en la nube pueden ser empresas, individuos e incluso estudiantes.

En el mundo del cómputo en la nube existen proveedores de servicios y consumidores que fueron explicados anteriormente, además de esto también hay distintos tipos de servicios y en cualquiera de estos tanto el proveedor como el consumidor tienen responsabilidades como las vemos en el siguiente cuadro:

![4](https://github.com/datalytics-mejorcondatos/AZ900-Azure-Fundamentals/blob/Develop/Material/Imagenes/4.png)

En el ambiente **On-Premise** se hace uso de servidores y entorno físico de la empresa, por esto en el cuadro vemos que todas las responsabilidades son de el consumidor en este caso la empresa. 


### Responsabilidades por servicio (IaaS, PaaS, SaaS)

 | Usuario | Proveedor |
 |---|---|
 | La información y los datos almacenados en la nube. | El centro de datos físico. |
 | Los dispositivos que pueden conectarse a la nube (teléfonos móviles, equipos, etc.). | La red física. |
 | Las cuentas e identidades de las personas, servicios y dispositivos de la organización. | Los hosts físicos. |

**Modelo de servicio** Este determinará la responsabilidad de cosas como
- Sistemas operativos 
- Controles de red 
- Aplicaciones
- Identidad e infraestructura 

## 2. Ventajas de utilizar servicios en nube

- ### Alta disponibilidad y escalabilidad en la nube

**Alta disponibilidad:** Siempre van a haber servicios de nube habilitados independientemente de si ocurre un evento que ponga en peligro una región de Azure debido a que hay otra región que la respalda. 


Existe algo llamado **Service Level Agreement (SLA)** que es el porcentaje de rendimiento que dice Azure, como proveedor de servicios de la nube que le brinda a los usuarios.  

**Escalabilidad:** Es la capacidad de un recurso para ajustarse a la demanda. 

**Escalabilidad horizontal:** Agrego más equipos de cómputo para solventar el salto o caída significativos en la demanda del recurso que se usa.
**Escalabilidad vertical:** Mejoras el recurso de Azure aumentando el almacenamiento, la memoria, etc. con el fin de tener más potencia en el procesamiento.

- ### Confiabilidad y previsibilidad en la nube


***Confiabilidad:*** Se refiere a la capacidad que tiene un sistema de recuperarse de los errores o fallos y seguir funcionando. 

***Previsibilidad:***  La previsibilidad se viene anclada de dos términos específicos:

1. **Previsibilidad de rendimiento**: Se refiere a predecir los recursos necesarios que podría utilizar un cliente. 


2.**Previsibilidad de costos:** Consta en pronosticar el costo del gasto en la nube. Se permite el seguimiento del uso de recursos en tiempo real, supervisar los recursos para asegurarse de que los usa de la manera más eficaz y aplicar análisis de datos para buscar patrones y tendencias que ayuden a planear mejor las implementaciones de recursos.
- ### Seguridad y gobernanza en la nube

La gobernanza le brinda mecanismos al usuario para poder mantener sus aplicaciones y recursos controlados. 

En cuanto a la seguridad,existen soluciones para controlarla al máximo.

## 3. Tipos de servicios en nube

- ### [Infraestructura como servicio (IaaS)](https://learn.microsoft.com/es-mx/training/modules/describe-cloud-service-types/2-describe-infrastructure-service)

El proveedor, en este caso Azure se encarga de  mantener el hardware, la conectividad de red (a Internet) y la seguridad física del espacio en el cual presta los servicios.

Por otro lado, el usuario tiene las siguientes responsabilidades:

 | Responsabilidades del usuario|
 |---|
 |Información y datos|
 |Dispositivos (móviles y PCs)|
 |Cuentas e identidades|
 |Ifraestructura de identidad y directorio|
 |Aplicaciones|
 |Controles de red|


Este tipo de servicio en la nube es muy **flexible** al usuario. 

- ### [Plataforma como servicio (PaaS)](https://learn.microsoft.com/es-mx/training/modules/describe-cloud-service-types/3-describe-platform-service)

El proveedor, en este caso Azure asume la responsabilidad del mantenimiento del sistema operativo para el uso de los servicios que quiero adquirir.

En cuanto a las responsabilidades tenemos:

 | Usuario | Proveedor |
 |---|---|
 | Información y datos | Sistema operativo |
 | Dispositivos (móviles y PCs) | Host y redes físicas |
 | Cuentas e identidades | Centro de datos |

- ### [Software como servicio (SaaS)](https://learn.microsoft.com/es-mx/training/modules/describe-cloud-service-types/4-describe-software-service)

Este tipo de servicio es muy común entre los usuarios de internet ya que el correo electrónico, las aplicaciones financieras, las de mensajería, etc., hacen parte de todos estos softwares como servicio. 

SaaS es el tipo de servicio más completo como producto, sin embargo, es el menos flexible.

Aquí se le atribuyen la mayor cantidad de responsabilidades al proveedor:

 | Responsabilidades del proveedor |
 |---|
 | Infraestructura de identidad y directorio |
 | Aplicaciones |
 | Controles de red |  
 | Sistema operativo |
 | Host físico |
 | Red física |
 | Centro de datos físico | 


- ### Clasificación de recursos por tipo de servicio

Para empezar a trabajar con proveedores de servicio en la nube, es importante reconocer los recursos clasificados por tipo de servicio. Aquí un a breve clasificación: 

![5](https://github.com/datalytics-mejorcondatos/AZ900-Azure-Fundamentals/blob/Develop/Material/Imagenes/5.png)