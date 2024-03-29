# Arquitectura y servicios de Azure
## 1. Componentes arquitectónicos de Azure
- ### Regiones
Una región es un área geográfica donde Azure, o en general un proveedor de servicios en la nube tiene al menos un centro de datos físico.
A continuación, los puntos azules son los centros de datos físicos con los que cuenta Azure al rededor del mundo.

![6](../Imagenes/6.png)

Gracias a estos centros de datos distribuidos estratégicamente, se garantiza que los servicios de Azure de una región ofrezcan el mejor rendimiento y seguridad.
Aunque algunos servicios de las máquinas virtuales solo están disponibles en determinadas regiones, como tipos de almacenamiento o tamaños de maquinas virtuales específicos. También hay algunos servicios globales de Azure que no requieren que seleccione una región concreta.

Si quieres tener una exploración de estas regiones puedes ingresar a la página oficial: https://infrastructuremap.microsoft.com/

- ### Zonas de disponibilidad

 Las zonas de disponibilidad son centros de datos separados físicamente dentro de una región de Azure. Las zonas de disponibilidad están conectadas a través de redes de fibra óptica de alta velocidad privadas como se muestra en la figura:
 
 ![7](../Imagenes/7.png)

Estas zonas de disponibilidad tienen un propósito y es proteger la información que un centro de datos tiene en caso de un desastre natural que afecte una zona, respaldando y haciendo una copia en otra zona de disponibilidad.
También hay otros tipos de usos entre zonas de disponibilidad como darle mayor rendimiento a un recurso. 
Las zonas de disponibilidad son principalmente para las máquinas virtuales, los discos administrados, los equilibradores de carga y las bases de datos SQL.  

Los servicios de Azure que admiten zonas de disponibilidad se dividen en tres categorías: 

- **Servicios de zona:** ancle el recurso a una zona específica (por ejemplo, máquinas virtuales, discos administrados, direcciones IP). 
- **Servicios de redundancia de zona:** la plataforma se replica automáticamente entre zonas (por ejemplo, almacenamiento con redundancia de zona, SQL Database). 
- **Servicios no regionales:** los servicios siempre están disponibles en las ubicaciones geográficas de Azure y son resistentes a las interrupciones de toda la zona, así como a las de toda la región. 

Incluso con la resistencia adicional que proporcionan las zonas de disponibilidad, es posible que un evento pueda ser tan grande que afecte a varias zonas de disponibilidad en una sola región. Para proporcionar una mayor resistencia, Azure tiene pares de regiones. 
- ### Pares de regiones

Una región se empareja con otra de la misma zona geográfica (debe estar a mínimo 500 km de distancia) para replicar recursos con el fin de respaldar la región y la información que maneja de eventos que puedan interrumpir el funcionamiento normal de la región y las zonas de disponibilidad.


- ###  Recursos y grupos de recursos

![8](../Imagenes/8.png)

#### Características 
* **Alta disponibilidad:** Los servicios de nube están habilitados independientemente de si ocurre un evento que ponga en peligro una región de Azure. 
* **Tolerancia a fallos:** Se aprende del error y sse trabaja sobre el mismo para la mejora. Siempre va a estar disponible la información.
* **Agilidad:** La creación de distintas tareas es rápida dado que los recursos que se tienen ahí minimizan la complejidad.
* *[Elasticidad:](https://azure.microsoft.com/en-gb/resources/cloud-computing-dictionary/what-is-elastic-computing/)* Un recurso se autoescala para cubrir las necesidades que se presenten. Esta característica se produce de forma automática. 

- ### Suscripciones
![9](../Imagenes/9.png)


Las suscripciones en Azure funcionan para organizar los recursos y grupos de recursos con el fin de tener un control organizado de la facturación. Existen varias modalidades de suscripciones que implican tener una autenticación y autorización para el uso de recursos. 

Una suscripción de Azure se vincula a una cuenta de Azure, que es una identidad en *Azure Active Directory (Azure AD)* o en un directorio en el que Azure AD confía.

Una cuenta puede tener varias suscripciones.
 Puede usar las suscripciones de Azure para definir límites en torno a los productos, servicios y recursos de Azure. Hay dos tipos de límites de suscripción que puede utilizar:

1. **Límite de facturación:** Se tiene en cuenta el uso de los productos de Azure. Azure genera facturas e informes de facturación independientes para cada suscripción, de modo que pueda organizar y administrar los costos.

2. **Límite de control de acceso:** Este modelo de facturación le permite administrar y controlar el acceso a los recursos que los usuarios aprovisionan con suscripciones específicas.

- ### Jerarquías 
La jerarquía es una forma flexible de organizar los recursos de acuerdo con el tipo de suscripción que hay entre los usuarios de una empresa que adquiere productos del cómputo en la nube. Un ejemplo es el siguiente diagrama:

![10](../Imagenes/10.png)

## 2. Servicios informáticos y de red de Azure

- ### Tipos de computación, máquinas virtuales y contenedores

**Contenedores:** Un contenedor es un paquete que tiene una aplicación con los elementos necesarios para su ejecución. 
El contenedor se puede encender como una máquina virtual, sin embargo no cuenta con un sistema operativo completo sino solo con los elementos necesarios.
Su tiempo de ejecución es de pocos segundos y es posible que yo pueda utilizar muchos contenedores en una máquina virtual. 

**Máquinas virtuales:** Este tipo de recursos le permiten a un usuario o empresa, implementar aplicaciones y programas informáticos en un sistema operativo virtualizado ya que la máquina virtual funciona como un computador en la nube.
### Servicios de cómputo bajo demanda donde podemos encontrar por ejemplo los siguientes: 

![a](../Imagenes/a.png)

Los servicios del ejemplo son Infraestructuras como Servicios (IaaS) o Plataformas como Servicios (PaaS). 

¿Cómo crear una [máquina virtual](https://learn.microsoft.com/es-mx/training/modules/describe-core-architectural-components-of-azure/7-exercise-create-azure-resource)?

Lo principal que hay que saber es que Azure te pide cuatro cosas fundamentales en los recursos:

        1. Suscripción: La cuenta en la que se va a cargar el costo.
        2. Grupo de recursos: Es una carpeta en la cual está el recurso que quieres usar, en esta carpeta puede haber muchos recursos, sin embargo, ningún recurso se puede repetir en otros grupos de recursos.
        3. Nombre: Nombre para el recurso, en este caso un nombre para la máquina virtual 
        4. Región: Área geográfica donde quieres que esté el recurso.

        - Azure virtual Machines Scale sets: Agrupa las máquinas virtuales para aumentarles el almacenamiento, la memoria para mejorar el rendimiento.
        - Azure Batch: Sirve para ejecutar tareas que necesitan un alto rendimiento como por ejemplo simulaciones, procesamiento de videos, transformación de datos, etc.

Existen una cantidad grande de recursos con distintas funcionalidades así que es recomendable hacer una exploración profunda a los recursos. De acuerdo a tu rol en la empresa, usarás diferentes recursos.
- ### Redes virtuales

Todos los servicios que ofrece Azure respecto a las redes virtuales son Infraestructuras como Servicio. 

A continuación presentaremos algunos ejemplos dentro de estos recursos:

![b](../Imagenes/b.png)

- *Azure virtual networks:* Permiten que los recursos de Azure se comuniquen entre sí.
- *Azure VPN Gateway:* Es una red privada virtual que mantiene la seguridad de la información almacenada en los recursos de Azure.
- *Azure Application* Distribuye equitativamente las cargas de ejecución al asignar tareas.  

De nuevo, este es solo un ejemplo de este tipo de recursos pero se deja al lector inspeccionar los demás servicio de redes virtuales. 

Se recomienda realizar el ejercicio de [configuración de acceso de red](https://learn.microsoft.com/es-mx/training/modules/describe-azure-compute-networking-services/9-exercise-configure-network-access). 
 
 
- ### Puntos finales públicos y privados

Las redes virtuales de Azure admiten puntos de conexión públicos y privados para permitir la comunicación entre recursos externos o internos con otros recursos internos.

- Los puntos de conexión públicos tienen una dirección IP pública y son accesibles desde cualquier parte del mundo.
- Los puntos de conexión privados existen dentro de una red virtual y tienen una dirección IP privada en el espacio de direcciones de esa red virtual.

## 3. Servicios de almacenamiento
- ### Comparación de servicios de almacenamiento

Los servicios de almacenamiento guardan objetos.

![c](../Imagenes/c.png)
 

1. **[Azure blob storage:](https://azure.microsoft.com/en-us/products/storage/blobs/)** 

Un almacén de objetos que se puede escalar de forma masiva para datos de texto y binarios. No hay restricción en el tipo de datos que contiene.  
Ventaja: no requiere que los desarrolladores piensen en discos o administren los discos ya que azure se encarga de las necesidades de almacenamiento físico. 
En blob storage puedo hacer: 
- Visualización de imágenes o documentos directamente en un explorador. 
- Almacenamiento de archivos para acceso distribuido. 
- Streaming de audio y vídeo. 
- Almacenamiento de datos para copia de seguridad y restauración, recuperación ante desastres y archivado. 
- Almacenamiento de datos para el análisis en local o en un servicio hospedado de Azure.  

Niveles de acceso de almacenamiento de blobs: 
 - Nivel de acceso frecuente: optimizado para almacenar datos a los que se accede con frecuencia (por ejemplo, imágenes para el sitio web). 
 - Nivel de acceso esporádico: optimizado para datos a los que se accede con poca frecuencia y que se almacenan al menos durante 30 días (por ejemplo, las facturas de los clientes). 
 - Nivel de acceso de archivo: conveniente para datos a los que raramente se accede y que se almacenan durante al menos 180 días con requisitos de latencia flexibles (por ejemplo, copias de seguridad a largo plazo). 

2. **[Azure file storage:](https://azure.microsoft.com/en-us/products/storage/files/)**

Recursos compartidos de archivos administrados mediante implementaciones locales y en la nube.  
**[¿Qué es un recurso compartido?](https://learn.microsoft.com/es-es/azure/architecture/hybrid/azure-file-share)**
### Usos

- Reemplazar o complementar servidores de archivos locales
- Aplicaciones "Lift-and-shift": facilita la migración mediante "lift and shift" de aplicaciones a la nube que espera un recurso compartido de archivos para almacenar datos de la aplicación de archivos o de un usuario.
- Simplifica el desarrollo en la nube
- Los recursos compartidos de archivos de Azure se pueden usar como volúmenes persistentes para contenedores con estado.

3. **[Azure disk storage:](https://azure.microsoft.com/en-us/products/storage/disks/)**

volúmenes de almacenamiento en el nivel de bloque para máquinas virtuales de Azure.  
Conceptualmente, son iguales que un disco físico, pero están virtualizados, lo que ofrece mayor resistencia y disponibilidad que un disco físico. Con los discos administrados, lo único que debe hacer es aprovisionar el disco; Azure se encargará del resto. 

4. **[Azure table storage:](https://azure.microsoft.com/en-us/products/storage/tables/)**

Se utiliza para almacenar petabytes de datos semiestructurados. Table Storage le permite escalar sin tener que fragmentar manualmente su conjunto de datos.
El almacenamiento con redundancia geográfica permite que los datos almacenados se repliquen tres veces dentro de una región y tres veces más en otra región, a cientos de kilómetros de distancia.


5. **[Azure queue storage:](https://azure.microsoft.com/es-es/products/storage/queues/)**

Es un servicio de almacenamiento para  mensajería. 
Sirve para crear aplicaciones con funciones separadas y reparta las cargas de trabajo.


6. **[Azure data lake:](https://azure.microsoft.com/es-mx/products/data-lake-analytics/)**

Es un servicio que facilita a los desarrolladores, los científicos de los datos y los analistas el almacenamiento de datos de cualquier tamaño, forma y velocidad, y para llevar a cabo todo tipo de procesamiento y análisis en diferentes plataformas y lenguajes. Azure Data Lake funciona con inversiones de TI para identidad, gobernanza y seguridad, consiguiendo una gobernanza y gestión de datos simplificadas. 

### [Ejercicio de creación de un blob de almacenamiento](https://learn.microsoft.com/es-mx/training/modules/describe-azure-storage-services/5-exercise-create-storage-blob)

- ### Opciones de redundancia
#### Describir la redundancia de almacenamiento de Azure 

La redundancia garantiza que la cuenta de almacenamiento cumple sus objetivos de disponibilidad  y durabilidad, aunque se produzcan errores. 
 
Factores a tener en cuenta para elegir la opción de redundancia más adecuada:  

    - Bajo costo 
    - Disponibilidad 
            - Cómo se replican los datos en la región primaria. 
            - Si los datos se replican en una segunda ubicación que está alejada geográficamente de la región primaria, para protegerse frente a desastres regionales. 
            - Si la aplicación necesita acceso de lectura a los datos replicados en la región secundaria en caso de que la región primaria deje de estar disponible. 

#### Redundancia en la región primaria 
Los datos se replican tres veces en la región primaria. 

Opciones para replicar datos en esta región son:  

1. **Almacenamiento con redundancia local (LRS):** Replica los datos tres veces dentro de un único centro de datos en la región primaria. LRS ofrece una durabilidad mínima de 11 nueves (99,999999999 %) de los objetos en un año determinado.  
        - Bajo costo 
        - Menor durabilidad 
        - Si se produce un desastre como un incendio o una inundación en el centro de datos, es posible que todas las réplicas de una cuenta de almacenamiento con LRS *se pierdan o no se puedan recuperar.*  

2. **Almacenamiento con redundancia de zona (ZRS):**  Para las regiones con zona de disponibilidad habilitada, el almacenamiento con redundancia de zona (ZRS) replica los datos de Azure Storage sincrónicamente en tres zonas de disponibilidad de Azure en la región primaria. ZRS proporciona a los objetos de datos de Azure Storage una durabilidad de al menos 12 nueves (99,9999999999 %) durante un año determinado.  

        - Si una zona no está disponible, Azure hace actualizaciones de red. 
        - Uso para escenarios con alta disponibilidad. 
        - ZRS para restringir la replicación de datos de acuerdo a requisitos de gobernanza de datos. 

#### Redundancia en la región secundaria

1. **Almacenamiento con redundancia geográfica (GRS):** Ejecuto un almacenamiento con redundancia local en dos regiones distintas. Región 1 y Región 2. 

2. **Almacenamiento con redundancia de zona geográfica (GZRS):** Ejecuto redundancia de zona en la región primaria y redundancia de zona local en la región secundaria. 

#### Almacenamiento con redundancia geográfica (GRS)

![d](../Imagenes/d.png)

El almacenamiento con redundancia geográfica (GRS) copia los datos tres veces en una ubicación física de la región primaria a través de almacenamiento con redundancia local y luego copia los datos a una región secundaria por el mismo tipo de almacenamiento.  

#### Almacenamiento con redundancia de zona geográfica (GZRS)

Los datos con una GZRS se almacenan en tres zonas de disponibilidad en la región primaria y luego se replican en una región geográfica secundaria para protegerlos de desastres regionales. 

![e](../Imagenes/e.png)
- ### Cuenta de almacenamiento y tipos de almacenamiento

### Azure Storage y sus servicios

### Ventajas 

- **Duradero y altamente disponible** La redundancia garantiza que los datos estén seguros en caso de producirse errores de hardware transitorios. También puede optar por replicar datos entre centros de datos o regiones geográficas para obtener protección adicional frente a catástrofes locales o desastres naturales. Los datos replicados de esta manera permanecen con una alta disponibilidad en caso de que se produzca una interrupción inesperada. 

- **Seguro** Todos los datos escritos en una cuenta de Azure Storage se cifran mediante el servicio. Azure Storage proporciona un control pormenorizado sobre quién tiene acceso a los datos. 

- **Escalable** Azure Storage está diseñado para poderse escalar de forma masiva para satisfacer las necesidades de rendimiento y almacenamiento de datos de las aplicaciones de hoy en día. 

- **Administrado** Azure controla automáticamente el mantenimiento, las actualizaciones y los problemas críticos del hardware. 

- **Accesible** Es posible acceder a los datos de Azure Storage desde cualquier parte del mundo a través de HTTP o HTTPS. Microsoft proporciona bibliotecas cliente para Azure Storage en diversos lenguajes, incluidos .NET, Java, Node.js, Python, PHP, Ruby, Go y otros, así como una API REST consolidada. Azure Storage admite la escritura en Azure PowerShell o la CLI de Azure. Y Azure Portal y el Explorador de Azure Storage ofrecen soluciones visuales sencillas para trabajar con los datos. 

- ### Migración

#### Azure Migrate 

Es un servicio que migra datos desde el entorno local a la nube. 

        - Plataforma de migración unificada:Un único portal para iniciar, ejecutar y realizar un seguimiento de la migración a Azure. 

        - Rango de herramientas: Rango de herramientas para la evaluación y migración Las herramientas de Azure Migrate incluyen Azure Migrate: Discovery y assessment y Azure Migrate: Server Migration. Azure Migrate también se integra con otros servicios y herramientas de Azure, así como con ofertas de proveedores de software independientes (ISV). 

        - Assessment and migration (Evaluación y migración): en el centro de Azure Migrate, puede evaluar y migrar la infraestructura local a Azure. 

### HERRAMIENTAS PARA LA MIGRACIÓN DE DATOS: 

- **Azure Migrate:** Discovery and assessment (Azure Migrate: detección y evaluación). Detecte y evalúe servidores locales que se ejecutan en VMware, Hyper-V y servidores físicos para preparar la migración a Azure. 

- **Web app migration assistant (Asistente de migración de aplicación web).** Azure App Service Migration Assistant es una herramienta independiente para evaluar sitios web locales para la migración a Azure App Service. Use Migration Assistant para migrar aplicaciones web de .NET y PHP a Azure. 

- **Azure Data Box.** Use los productos de Azure Data Box para trasladar grandes cantidades de datos sin conexión a Azure. 


## 4. Identidad, acceso y seguridad de Azure
- ### Servicios de directorio de Azure
 
#### Azure Active Directory (Azure AD)

Es un directorio donde es posible acceder a las aplicaciones en la nube de Microsoft o a otra nube. 
Cuando usamor Active Directory ejecutado en Windows Server, es posible tener un servicio de administración de acceso a los servicios que ha adquirido la empresa. Es posible controlar las cuentas de identidad que se tienen para acceder globalmente a la nube.

Los usuarios de Azure Active Directory son:
- Administradores de TI
- Desarrolladores de aplicaciones
- Usuarios
- Suscriptores de servicios en línea

Cada uno de los usuarios anteriormente mencionados tienen diferentes funciones que les permite tener Azure AD de acuerdo con sus necesidades.

Es importante recalcar que Azure Active Directory brinda servicios de autenticación, es decir, comprobar la identidad al ingresar a alguna aplicación o recurso. También se tiene un inicio de sesión único (SSO) donde basta con tener un solo usuario y contraseña para hacer uso de estos recursos.  Por otro lado, administrar las aplicaciones tanto en la nube como las locales es una ventaja que tiene Azure AD. Por último y no menos importante, la posibilidad de registrar dispositivos y administrarlos es otra forma de acceso a los recursos.

#### Azure Active Directory Domain Services (Azure AD DS)

Este es un servicio que brinda servicios de dominio administrados sin tener que mantener una infraestructura que lo admita. Algunos de los servicios son los siguientes:
- Unión a un dominio
- Directivas de grupo
- Protocolo ligero de acceso a directorios (LDAP) 
- Autenticación de Kerberos/NTLM

Azure AD DS se integra con Azure AD  con el fin de que los usuarios inicien sesión en lso servicios y las aplicaciones conectados al dominio. 
Esto proporciona una migración mediante [lift-and-shift](https://learn.microsoft.com/es-es/dotnet/architecture/modernize-with-azure-containers/lift-and-shift-existing-apps-azure-iaas) de los recursos locales de azure.
- ### Métodos de autenticación

Cuando hablamos de autenticación, básicamente nos referimos a demostrar quien dice ser que es. Existen distintos métodos de autenticación:

- **Inicio de sesión único**: 

Este método de autenticación permite a los usuarios iniciar sesión una vez y utilizar credenciales para acceder a los recursos. Es importante tener en cuenta que este método de autenticación empieza a funcionar cuando las aplicaciones confíen en un identificador inicial. 

Usar el inicio de sesión único en las cuentas permite a los usuarios administrar su identidad y al equipo de TI gestionar los usuarios con mayor facilidad.


- **Autenticación multifactor - MFA**

Este tipo de autenticación consiste en solicitar a un usuario, una forma adicional (factor) de comprobar la identificación en el momento de iniciar sesión. Esta autenticaciónpermite proteger la cuenta en situaciones en las cuales la contraseña por sí sola estuvo en riesgo.

La autenticación multifactor proporciona seguridad adicional a las identidades, ya que se requieren dos o más elementos para una autenticación completa. Estos elementos se dividen en tres categorías:

        - Algo que el usuario sabe: puede ser una pregunta de seguridad.
        - Algo que el usuario tiene: se puede tratar de un código que se envía al teléfono móvil del usuario.
        - Algo que el usuario es: normalmente, algún tipo de propiedad biométrica, como la huella dactilar o el escaneo facial.


- **Azure AD Multi-factor Authentication**

Este método es un servicio propio de Microsoft en donde se aplica la lógica de autenticación multifactor y permite elegir la forma adicional de inicio de sesión, como por ejemplo una llamada de teléfono o una notificación de aplicación móvil.

- **Autenticación sin contraseña**

Este método es muy cómo dado que la contraseña se reemplaza por algo que se es o algo que se sabe. En la autenticación sin contraseña hay que configurar su cuenta con un dispositivo que esté asociado. Ahora que se conoce el dispositivo, una vez que proporcione algo que sepa o sea (por ejemplo, un PIN o una huella digital), se podrá autenticar sin usar una contraseña.

- ### Identidades externas y acceso de invitados

Una identidad externa es una persona, un dispositivo, un servicio, etc. que está fuera de la organización. Azure AD External Identities hace referencia a todas las formas en que puede interactuar de forma segura con usuarios externos a su organización. Si quiere colaborar con asociados, distribuidores o proveedores, puede compartir los recursos y definir cómo los usuarios internos pueden acceder a organizaciones externas. Si es un desarrollador que crea aplicaciones orientadas al consumidor, puede administrar las experiencias de identidad de los clientes.

- ### Acceso condicional

Esta herramienta permite acceso a distintos recursos en función de señales de identidad. Este tipo de autenticación puede solicitarle a un usuario un segundo factor si este no e encuentra en una ubicación conocida. 

Esta herramienta toma desiciones basadas en señales del usuario que son recopiladas con el fin de de permitir o denegar accesos. 
Estas decisiones se pueden ver en el siguiente diagrama:

![f](../Imagenes/f.png)

En función de estas señales, la decisión puede ser permitir el acceso completo si el usuario inicia sesión desde su ubicación habitual. Si el usuario inicia sesión desde una ubicación inusual o una ubicación marcada como de alto riesgo, el acceso puede bloquearse por completo, o bien podría concederse después de que el usuario proporcione una segunda forma de autenticación.
- ### Control de acceso

Azure permite controlar el acceso a ciertos recursos o funciones de distintos usuarios con el control basado en roles de Azure (RBAC de Azure). 

Azure brinda roles integrados que especifica los requisitos de acceso comunes de los recursos de la nube de acuerdo con las necesidades de la empresa. 

A continuación se tiene un diagrama que especifica los roles y los ámbitos en los cuales se van concediendo permisos manteniendo el control de acceso de los usuarios. 

![g](../Imagenes/g.png)


En función de estas señales, la decisión puede ser permitir el acceso completo si el usuario inicia sesión desde su ubicación habitual. Si el usuario inicia sesión desde una ubicación inusual o una ubicación marcada como de alto riesgo, el acceso puede bloquearse por completo, o bien podría concederse después de que el usuario proporcione una segunda forma de autenticación.

- ### Confianza sero

Es un modelo de seguridad que espera el peor de los escenarios posibles y de acuerdo con eso protege los recursos. Confianza cero presupone que hay una vulneración y comprueba todas las solicitudes como si provinieran de una red no controlada.

En la actualidad, las organizaciones necesitan un modelo de seguridad nuevo que se adapte eficazmente a la complejidad del entorno moderno, adopte los recursos móviles y proteja a personas, dispositivos, aplicaciones y datos dondequiera que se encuentren.

Para abordar este nuevo mundo informático, Microsoft recomienda encarecidamente el modelo de seguridad de Confianza cero, que se basa en estos principios rectores:

Comprobar explícitamente: realice siempre las operaciones de autorización y autenticación en función de todos los puntos de datos disponibles.
Usar el acceso de privilegios mínimos: limite el acceso de los usuarios con Just-in-Time y Just-Enough-Access (JIT/JEA), directivas que se adaptan al nivel de riesgo y protección de datos.
Asumir que hay brechas: minimice el radio de expansión y el acceso a los segmentos. Comprobación del cifrado de un extremo a otro. Utilice el análisis para obtener visibilidad, impulsar la detección de amenazas y mejorar las defensas.


- ### Modelo de defensa en profundidad

La defensa en profundiad tiene como objetivo principal la protección de la información para que no accedan personas no autorizadas a los distintos recursos. 

Azure tiene implementados distintos mecanismos con el fin de ralentizar un posible ataque con el fin de sustraer información que está altamente protegida.

Para facilidad del lector se tiene el siguiente diagrama que esquematiza de forma sencilla la protección a la información en distintas capas.

![h](../Imagenes/h.png)

Para poder entender mejor este [modelo de defensa en profundidad](https://learn.microsoft.com/es-mx/training/modules/describe-azure-identity-access-security/8-describe-defense-depth) es necesario hacer una lectura más detallada.

- ### Microsoft Defender for Cloud

Esta herramienta sirve para supervisar la administración de la seguridad y la protección contra amenazas que se tiene, supervisando la nube, los entornos locales, los entornos híbridos y la multinube con el propósito de mandar instrucciones y proporcionar notificaciones que garanticen la posición de seguridad.

En dado caso que se cuente con un centro de datos local o incluso en la nube, Defender for Cloud puede implementar un agente de Log Analytics para recopilar datos relacionados con la seguridad de estos centros de datos.

Defender for Cloud le permite detectar amenazas en:

- **Servicios de PaaS de Azure:** puede detectar amenazas dirigidas a servicios de Azure como Azure App Service, Azure SQL, la cuenta de Azure Storage y otros servicios de datos. También puede realizar la detección de anomalías en los registros de actividad de Azure mediante la integración nativa con Microsoft Defender para aplicaciones en la nube (anteriormente conocido como Microsoft Cloud App Security).
- **Servicios de datos de Azure:** Defender for Cloud incluye capacidades que le ayudarán a clasificar automáticamente los datos en Azure SQL. También puede obtener evaluaciones de las posibles vulnerabilidades en los servicios de Azure SQL y Azure Storage, además de recomendaciones sobre cómo mitigarlas.
- **Redes:** Defender for Cloud le permite limitar la exposición a los ataques por fuerza bruta. Si reduce el acceso a los puertos de las máquinas virtuales mediante el acceso de máquina virtual Just-In-Time, puede proteger la red al prevenir el acceso innecesario. Puede establecer directivas de acceso seguro en los puertos seleccionados, solo para usuarios autorizados, direcciones IP o intervalos de direcciones IP de origen permitidos y durante un período limitado.