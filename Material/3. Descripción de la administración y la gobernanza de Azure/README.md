# 1. Gestión de costes en Azure

- ### Factores que afectan los costes

Azure maneja un modelo de gastos operativos (OpEx) y estos gastos puedes verse afectados por muchos factores como los nombrados a continuación:

- **Tipo de recurso:**

Al referirse a los tipos de recursos, incluyendo la configuración y las regiones en las cuales están estos recursos, se habla también de las instancias que son creadas por Azure para medir el uso con el fin de generar un registro y poder calcular la factura. Las anteriores características de un recurso en Azure pueden afectar en el costo de facturación porque hay que tener en cuenta las especificaciones que se escojan para tener un mayor rendimiento.


- **Consumo:**

El modelo de pago en la nube implica pagar por los recursos que se usa, es decir, si uso más proceso pago más y viceversa. Este mecanismo de precios es bastante flexible. Además, Azur ofrece al usuario comprometerse para usar una cantidad específica de recursos y recibir descuesto en otros recursos reservados. Esto es una forma de ahorro que tiene este compromiso.

- **Mantenimiento:**

Es posible tener todos los recursos organizados con el fin de controlar los costos de los recursos de la nube.  Al vigilar los recursos y asegurarse de que no mantiene los que ya no son necesarios, puede ayudar a controlar los costos de la nube y ni pagar de más.

- **Geography:**

Al crear un recurso de Azure, este debe definir la región en la cual se implementará el recurso. Aquí se aplican las definiciones vistas previamente de zonas, regiones, etc., esto es importante dado que los precios del aprovisionamiento de los recursos varía según la zona especificada. La razón por la cual estos precios cambien es debido al costo de energía, la mano de obra, los impuestos en el país en el que la región se encuentra y demás tarifas.

- **Tipo de suscripción:**

Los tipos de suscripción también incluyen formas de aprovisionamiento que afecta en los costos de un recurso.

- **Azure Marketplace:**

Azure Marketplace le permite comprar soluciones basadas en Azure de proveedores de terceros. De esta manera no es Azure sino el proveedor quien establece las estructuras de facturación.

- ### Calculadora de precios

Azure cuenta con dos tipos de calculadoras con propósitos distintos donde se puede hacer una estimación de precios por uso:

- [**Calculadora de precios**](https://azure.microsoft.com/es-mx/pricing/calculator/): Esta calculadora está diseñada para dar un costo estimado en el aprovisionamiento de recursos en la nube. Se pueden hacer cálculos de recursos individuales incluyendo el proceso, almacenamiento, redundancia y nivel de acceso, u otros escenarios de acuerdo con las necesidades personales o de la empresa.

- [**Calculadora de TCO**](https://azure.microsoft.com/es-mx/pricing/tco/calculator/): Esta calculadora, por otro lado, está diseñada para comparar los costos de ejecución de una infraestructura local y una infraestructura en la nube, incluye costos de mano de obra de TI, energía, etc., para ver  qué precios maneja Azure. 

- ### Herramienta de gestión de costes y facturación

Cost Management proporciona la capacidad de comprobar rápidamente los costos de los recursos de Azure, crear alertas basadas en el gasto de recursos y crear presupuestos que se pueden usar para automatizar la administración de recursos.

El análisis de costos es un subconjunto de Cost Management que proporciona una vista rápida de los costos de Azure. Con el análisis de costos, puede ver rápidamente el costo total de varias maneras diferentes, incluido por ciclo de facturación, región, recurso, etc.

- ### Etiquetas

Las etiquetas de recursos son un buen método de organización de recursos puesto que proporcionan información adicional sobre los recurso.
Los metadatos que proporcionan las etiquetas sirven para:

- **Administración de recursos:** las etiquetas permiten localizar recursos asociados a cargas de trabajo, entornos, unidades de negocio y propietarios específicos y actuar al respecto.

- **Optimización y administración de costes:** las etiquetas permiten agrupar recursos para que podamos informar sobre los costes, asignar centros de costes internos, mantener los presupuestos a raya y predecir costes estimados.

- **Administración de operaciones:** las etiquetas permiten agrupar recursos según la importancia que tiene su disponibilidad para nuestro negocio. Esta agrupación nos ayuda a formular acuerdos de nivel de servicio (SLA), que constituyen una garantía de rendimiento o de tiempo de actividad entre nosotros y nuestros usuarios.

- **Seguridad:** las etiquetas permiten clasificar los datos según su nivel de seguridad, por ejemplo, públicos o confidenciales.

- **Gobernanza y cumplimiento normativo:** las etiquetas permiten identificar los recursos que cumplen con los requisitos de gobernanza o cumplimiento normativo, como la norma ISO 27001. Las etiquetas también pueden formar parte de nuestros esfuerzos de aplicación de estándares. Así, podríamos exigir que todos los recursos se etiqueten con un nombre de departamento o propietario.

- **Automatización y optimización de las cargas de trabajo:** las etiquetas pueden servir para ver todos los recursos que participan en implementaciones complejas. Por ejemplo, podemos etiquetar un recurso con su nombre de aplicación o carga de trabajo asociado y usar un software como Azure DevOps para realizar tareas automatizadas en esos recursos.

## 2. Funciones y herramientas de Azure para la gobernanza y el cumplimiento normativo
- ### Azure Blueprints

Azure Blueprints permite estandarizar las implementaciones que se tienen en el entorno o en la suscripción de Azur para definir una configuración repetible cin el fin de aplicarlas a medida que se vayan creando nuevas suscripciones. 


Un **artefacto** es un componente de un plano técnico. Blueprints implementa un nuevo entorno en funciones de los requisitos, opciones y configuraciones de los artefactos que tiene asociados. Los artefactos pueden incluir:

- Asignaciones de roles
- Asignaciones de directivas
- Plantillas de Azure Resource Manager
- Grupo de recursos


Con Azure Blueprints, la relación entre la definición del plano técnico (lo que debe ser implementado) y su asignación (lo que se ha implementado) permanece. En otras palabras, Azure crea un registro que asocia un recurso con el plano técnico que lo define, y gracias a esta conexión podemos realizar el seguimiento y la auditoría de nuestras implementaciones.

- ### Política de Azure

Azure Policy permite definir directivas individuales o directivas relacionadas, así Azure Policy evalúa los recursos que cumplen o no cumplen con las directivas readas. Es posible establecer directivas en un recurso, grupos de recursos, una suscripción, etc. 
Estas directivas se heredan lo que significa aplicar automáticamente a las otras agrupaciones esta directiva. 

Azure Policy incluye definiciones de iniciativas y directivas integradas para categorías como Almacenamiento, Redes, Proceso, Centro de Seguridad y Supervisión. También puede corregir automáticamente los recursos y configuraciones no conformes para garantizar la integridad del estado de los recursos. Adempas  se integra con Azure DevOps aplicando directivas de integración continua y canalización de entrega que competen a las fases de implementación anterior y posterior de las aplicaciones.

Una iniciativa es una forma de agrupar las directivas relacionadas. 

Las definiciones de directiva que aplican a una iniciativa son:

- **Supervisar base de datos SQL sin cifrar en Security Center:** esta directiva supervisa servidores y bases de datos SQL sin cifrar.
- **Supervisión de los puntos vulnerables del sistema operativo en Security Center:** esta directiva supervisa los servidores que no cumplen la línea base de la vulnerabilidad del sistema operativo configurada.
- **Supervisar la falta de Endpoint Protection en Security Center:** esta directiva supervisa los servidores que no tienen instalado un agente de Endpoint Protection.

- ### Bloqueos de recursos

La idea del bloqueo de recursos es impedir que se eliminen o se modifiquen por error los recursos. Este riesgo sigue existiendo así haya directivas de control de acceso basado en los roles debido a que una persona con un nivel de acceso permitido puede elimine recursos importantes. Los bloqueos de recursos se heredan, lo que significa que si coloca un bloqueo de recursos en un grupo de recursos, también se aplicará el bloqueo a todos los recursos dentro del grupo.

#### Tipos de bloqueos de recursos

Hay dos tipos de bloqueos de recursos, uno que impide que los usuarios eliminen un recurso y otro que impide que los usuarios lo cambien o eliminen.

- Eliminar significa que los usuarios autorizados pueden leer y modificar un recurso, pero no eliminarlo.
- ReadOnly significa que los usuarios autorizados solo pueden leer recursos, pero no actualizarlos ni eliminarlos. Aplicar este bloqueo es similar a restringir todos los usuarios autorizados a los permisos concedidos por el rol Lector.

#### Eliminar o cambiar un recurso bloqueado 

1. Quitar el bloqueo
2. Aplicar acciones de acuerdo a los permisos que se tienen.
3. Quitar el bloqueo y luego realizar la actividad bloqueada. 


Ingrese [aquí](https://learn.microsoft.com/es-mx/training/modules/describe-features-tools-azure-for-governance-compliance/5-exercise-configure-resource-lock) para realizar un ejercicio de configuración de un bloque de recursos.

- ### Portal de confianza de los servicios

Este portal proporciona contenido, herramientas y demás recursos sobre prácticas de seguirad, privacidad y cumplimiento de Microsoft. Este portal tiene detalles acerca de la implementación de controles y procesos de Microsoft que protegen los servicios en la nube.

¿Qupe c

## 3. Características y herramientas para la gestión y despliegue de recursos Azure

- ### Portal de Azure

Azure Portal proporciona una alternativa a las herramientas de línea de comandos. Azure Portal permite:

- Construir, administrar y supervisar todo, desde aplicaciones web sencillas hasta complejas implementaciones en la nube
- Crear paneles personalizados para una visualización organizada de los recursos
Configurar opciones de accesibilidad para una experiencia óptima- 

- ### Azure Cloud Shell

Azure Cloud Shell es una herramienta de Shell basada en explorador que permite crear, configurar y administrar recursos de Azure mediante un Shell. Azure Cloud Shell admite tanto Azure PowerShell como la interfaz de la línea de comandos (CLI) de Azure, que es un Shell de Bash.

- ### Azure Arc

Azure permite:

- Administrar todo el entorno mediante la proyección de los recursos existentes que no son de Azure en ARM.
- Administrar las máquinas virtuales híbridas y de varias nubes, los clústeres de Kubernetes y las bases de datos como si se ejecutaran en Azure.
- Usar los servicios y funcionalidades de administración de Azure que conozca, independientemente de dónde se encuentren.
- Seguir usando ITOps tradicionales al tiempo que se incorporan procedimientos de DevOps para admitir en el entorno patrones nuevos y nativos de nube.
- Configurar ubicaciones personalizadas como una capa de abstracción a partir del clúster de Kubernetes habilitado para Azure Arc y las extensiones de clúster.


- ### Azure Resource Manager

Por otro lado, Azure Resourse Manager permite administrar los recursos de tal forma que se pueda crear, actualizar y eliminar recursos de la cuenta. 

**Ventajas**:

-Administrar la infraestructura mediante plantillas declarativas en lugar de scripts. Una plantilla de Resource Manager es un archivo JSON que define lo que quiere implementar en Azure.
- Implementar, administrar y supervisar todos los recursos de la solución en grupo, en lugar de controlarlos individualmente.
- Vuelva a implementar la solución a lo largo del ciclo de vida de desarrollo y tenga la seguridad de que los recursos se implementan en un estado coherente.
- Defina las dependencias entre recursos de modo que se implementen en el orden correcto.
- Aplique control de acceso a todos los servicios, puesto que RBAC se integra de forma nativa en la plataforma de administración.
- Aplicar etiquetas a los recursos para organizar de manera lógica todos los recursos de la suscripción.
- Comprenda la facturación de la organización viendo los costos de un grupo de recursos que comparten la misma etiqueta.


## 4. Herramientas de supervición en Azure
- ### Azure Advisor 

Azure Advisor revalúa los recursos de Azure y trata de mejorar la confiabilidad, la seguridad y el rendimiento, lograr la excelencia operativa y reducir los costos en os recursos. Esto es posible ua que la idea es optimizar la nube ahorrandole tiempo al usuario. 

- ### Azure Service Health 

Azure Service Health le permite realizar un seguimiento de los recursos de Azure, tanto los recursos implementados específicamente como el estado general de Azure. Azure Service Health lo hace combinando tres servicios de Azure diferentes:

- **Estado de Azure** es una visión general del estado de Azure de forma global. Estado de Azure informa de las interrupciones de servicio en Azure en la página de estado de Azure . La página es una vista global del estado de todos los servicios y regiones de Azure. Es una buena referencia de los incidentes con un impacto generalizado.

- **Service Health** proporciona una vista más limitada del estado de los servicios y regiones de Azure. Se centra en los servicios y regiones de Azure que usa. Es el mejor lugar para buscar comunicaciones que afecten a los servicios relativas a interrupciones, actividades de mantenimiento planeado y otros avisos de mantenimiento, ya que tras la autenticación, Service Health conoce los servicios y recursos que usa en la actualidad. Incluso puede configurar las alertas de Service Health para que le envíen notificaciones cuando se produzcan problemas del servicio, mantenimientos planeados o cualquier otro cambio que pueda afectar a los servicios y regiones de Azure que usa.

- **Resource Health** es una vista personalizada de los recursos reales de Azure. Proporciona información sobre el estado de los recursos en la nube individuales, como una instancia de máquina virtual concreta. Mediante Azure Monitor también puede configurar alertas que le notifiquen los cambios de disponibilidad de los recursos en la nube.


- ### Azure Monitor 


![i](https://github.com/datalytics-mejorcondatos/AZ900-Azure-Fundamentals/blob/Develop/Material/Imagenes/i.png)

Azure Monitor es una plataforma para recopilar datos sobre los recursos, analizar esos datos, visualizar la información e incluso actuar en función de los resultados. Azure Monitor puede supervisar los recursos de Azure, los recursos locales e incluso los recursos de varias nubes, como las máquinas virtuales hospedadas con otro proveedor de nube.## 1. Gestión de costes en Azure

- ### Factores que afectan los costes

Azure maneja un modelo de gastos operativos (OpEx) y estos gastos puedes verse afectados por muchos factores como los nombrados a continuación:

- **Tipo de recurso:**

Al referirse a los tipos de recursos, incluyendo la configuración y las regiones en las cuales están estos recursos, se habla también de las instancias que son creadas por Azure para medir el uso con el fin de generar un registro y poder calcular la factura. Las anteriores características de un recurso en Azure pueden afectar en el costo de facturación porque hay que tener en cuenta las especificaciones que se escojan para tener un mayor rendimiento.


- **Consumo:**

El modelo de pago en la nube implica pagar por los recursos que se usa, es decir, si uso más proceso pago más y viceversa. Este mecanismo de precios es bastante flexible. Además, Azur ofrece al usuario comprometerse para usar una cantidad específica de recursos y recibir descuesto en otros recursos reservados. Esto es una forma de ahorro que tiene este compromiso.

- **Mantenimiento:**

Es posible tener todos los recursos organizados con el fin de controlar los costos de los recursos de la nube.  Al vigilar los recursos y asegurarse de que no mantiene los que ya no son necesarios, puede ayudar a controlar los costos de la nube y ni pagar de más.

- **Geography:**

Al crear un recurso de Azure, este debe definir la región en la cual se implementará el recurso. Aquí se aplican las definiciones vistas previamente de zonas, regiones, etc., esto es importante dado que los precios del aprovisionamiento de los recursos varía según la zona especificada. La razón por la cual estos precios cambien es debido al costo de energía, la mano de obra, los impuestos en el país en el que la región se encuentra y demás tarifas.

- **Tipo de suscripción:**

Los tipos de suscripción también incluyen formas de aprovisionamiento que afecta en los costos de un recurso.

- **Azure Marketplace:**

Azure Marketplace le permite comprar soluciones basadas en Azure de proveedores de terceros. De esta manera no es Azure sino el proveedor quien establece las estructuras de facturación.

- ### Calculadora de precios

Azure cuenta con dos tipos de calculadoras con propósitos distintos donde se puede hacer una estimación de precios por uso:

- [**Calculadora de precios**](https://azure.microsoft.com/es-mx/pricing/calculator/): Esta calculadora está diseñada para dar un costo estimado en el aprovisionamiento de recursos en la nube. Se pueden hacer cálculos de recursos individuales incluyendo el proceso, almacenamiento, redundancia y mnivel de acceso, u otros escenarios de acuerdo con las necesidades personales o de la empresa.

- [**Calculadora de TCO**](https://azure.microsoft.com/es-mx/pricing/tco/calculator/): Esta calculadora, por otro lado, está diseñada para comparar los costos de ejecución de una infraestructura local y una infraestructura en la nube, incluye costos de mano de obra de TI, energía, etc., para ver  qué precios maneja Azure. 

- ### Herramienta de gestión de costes y facturación

Cost Management proporciona la capacidad de comprobar rápidamente los costos de los recursos de Azure, crear alertas basadas en el gasto de recursos y crear presupuestos que se pueden usar para automatizar la administración de recursos.

El análisis de costos es un subconjunto de Cost Management que proporciona una vista rápida de los costos de Azure. Con el análisis de costos, puede ver rápidamente el costo total de varias maneras diferentes, incluido por ciclo de facturación, región, recurso, etc.

- ### Etiquetas

Las etiquetas de recursos son un buen método de organización de recursos puesto que proporcionan información adicional sobre los recurso.
Los metadatos que proporcionan las etiquetas sirven para:

- **Administración de recursos:** las etiquetas permiten localizar recursos asociados a cargas de trabajo, entornos, unidades de negocio y propietarios específicos y actuar al respecto.

- **Optimización y administración de costes:** las etiquetas permiten agrupar recursos para que podamos informar sobre los costes, asignar centros de costes internos, mantener los presupuestos a raya y predecir costes estimados.

- **Administración de operaciones:** las etiquetas permiten agrupar recursos según la importancia que tiene su disponibilidad para nuestro negocio. Esta agrupación nos ayuda a formular acuerdos de nivel de servicio (SLA), que constituyen una garantía de rendimiento o de tiempo de actividad entre nosotros y nuestros usuarios.

- **Seguridad:** las etiquetas permiten clasificar los datos según su nivel de seguridad, por ejemplo, públicos o confidenciales.

- **Gobernanza y cumplimiento normativo:** las etiquetas permiten identificar los recursos que cumplen con los requisitos de gobernanza o cumplimiento normativo, como la norma ISO 27001. Las etiquetas también pueden formar parte de nuestros esfuerzos de aplicación de estándares. Así, podríamos exigir que todos los recursos se etiqueten con un nombre de departamento o propietario.

- **Automatización y optimización de las cargas de trabajo:** las etiquetas pueden servir para ver todos los recursos que participan en implementaciones complejas. Por ejemplo, podemos etiquetar un recurso con su nombre de aplicación o carga de trabajo asociado y usar un software como Azure DevOps para realizar tareas automatizadas en esos recursos.

## 2. Funciones y herramientas de Azure para la gobernanza y el cumplimiento normativo
- ### Azure Blueprints

Azure Blueprints permite estandarizar las implementaciones que se tienen en el entorno o en la suscripción de Azur para definir una configuración repetible cin el fin de aplicarlas a medida que se vayan creando nuevas suscripciones. 


Un **artefacto** es un componente de un plano técnico. Blueprints implementa un nuevo entorno en funciones de los requisitos, opciones y configuraciones de los artefactos que tiene asociados. Los artefactos pueden incluir:

- Asignaciones de roles
- Asignaciones de directivas
- Plantillas de Azure Resource Manager
- Grupo de recursos


Con Azure Blueprints, la relación entre la definición del plano técnico (lo que debe ser implementado) y su asignación (lo que se ha implementado) permanece. En otras palabras, Azure crea un registro que asocia un recurso con el plano técnico que lo define, y gracias a esta conexión podemos realizar el seguimiento y la auditoría de nuestras implementaciones.

- ### Política de Azure

Azure Policy permite definir directivas individuales o directivas relacionadas, así Azure Policy evalúa los recursos que cumplen o no cumplen con las directivas readas. Es posible establecer directivas en un recurso, grupos de recursos, una suscripción, etc. 
Estas directivas se heredan lo que significa aplicar automáticamente a las otras agrupaciones esta directiva. 

Azure Policy incluye definiciones de iniciativas y directivas integradas para categorías como Almacenamiento, Redes, Proceso, Centro de Seguridad y Supervisión. También puede corregir automáticamente los recursos y configuraciones no conformes para garantizar la integridad del estado de los recursos. Adempas  se integra con Azure DevOps aplicando directivas de integración continua y canalización de entrega que competen a las fases de implementación anterior y posterior de las aplicaciones.

Una iniciativa es una forma de agrupar las directivas relacionadas. 

Las definiciones de directiva que aplican a una iniciativa son:

- **Supervisar base de datos SQL sin cifrar en Security Center:** esta directiva supervisa servidores y bases de datos SQL sin cifrar.
- **Supervisión de los puntos vulnerables del sistema operativo en Security Center:** esta directiva supervisa los servidores que no cumplen la línea base de la vulnerabilidad del sistema operativo configurada.
- **Supervisar la falta de Endpoint Protection en Security Center:** esta directiva supervisa los servidores que no tienen instalado un agente de Endpoint Protection.

- ### Bloqueos de recursos

La idea del bloqueo de recursos es impedir que se eliminen o se modifiquen por error los recursos. Este riesgo sigue existiendo así haya directivas de control de acceso basado en los roles debido a que una persona con un nivel de acceso permitido puede elimine recursos importantes. Los bloqueos de recursos se heredan, lo que significa que si coloca un bloqueo de recursos en un grupo de recursos, también se aplicará el bloqueo a todos los recursos dentro del grupo.

#### Tipos de bloqueos de recursos

Hay dos tipos de bloqueos de recursos, uno que impide que los usuarios eliminen un recurso y otro que impide que los usuarios lo cambien o eliminen.

- Eliminar significa que los usuarios autorizados pueden leer y modificar un recurso, pero no eliminarlo.
- ReadOnly significa que los usuarios autorizados solo pueden leer recursos, pero no actualizarlos ni eliminarlos. Aplicar este bloqueo es similar a restringir todos los usuarios autorizados a los permisos concedidos por el rol Lector.

#### Eliminar o cambiar un recurso bloqueado 

1. Quitar el bloqueo
2. Aplicar acciones de acuerdo a los permisos que se tienen.
3. Quitar el bloqueo y luego realizar la actividad bloqueada. 


Ingrese [aquí](https://learn.microsoft.com/es-mx/training/modules/describe-features-tools-azure-for-governance-compliance/5-exercise-configure-resource-lock) para realizar un ejercicio de configuración de un bloque de recursos.

- ### Portal de confianza de los servicios

Este portal proporciona contenido, herramientas y demás recursos sobre prácticas de seguirad, privacidad y cumplimiento de Microsoft. Este portal tiene detalles acerca de la implementación de controles y procesos de Microsoft que protegen los servicios en la nube.

¿Qupe c

## 3. Características y herramientas para la gestión y despliegue de recursos Azure

- ### Portal de Azure

Azure Portal proporciona una alternativa a las herramientas de línea de comandos. Azure Portal permite:

- Construir, administrar y supervisar todo, desde aplicaciones web sencillas hasta complejas implementaciones en la nube
- Crear paneles personalizados para una visualización organizada de los recursos
Configurar opciones de accesibilidad para una experiencia óptima- 

- ### Azure Cloud Shell

Azure Cloud Shell es una herramienta de Shell basada en explorador que permite crear, configurar y administrar recursos de Azure mediante un Shell. Azure Cloud Shell admite tanto Azure PowerShell como la interfaz de la línea de comandos (CLI) de Azure, que es un Shell de Bash.

- ### Azure Arc

Azure permite:

- Administrar todo el entorno mediante la proyección de los recursos existentes que no son de Azure en ARM.
- Administrar las máquinas virtuales híbridas y de varias nubes, los clústeres de Kubernetes y las bases de datos como si se ejecutaran en Azure.
- Usar los servicios y funcionalidades de administración de Azure que conozca, independientemente de dónde se encuentren.
- Seguir usando ITOps tradicionales al tiempo que se incorporan procedimientos de DevOps para admitir en el entorno patrones nuevos y nativos de nube.
- Configurar ubicaciones personalizadas como una capa de abstracción a partir del clúster de Kubernetes habilitado para Azure Arc y las extensiones de clúster.


- ### Azure Resource Manager

Por otro lado, Azure Resourse Manager permite administrar los recursos de tal forma que se pueda crear, actualizar y eliminar recursos de la cuenta. 

**Ventajas**:

-Administrar la infraestructura mediante plantillas declarativas en lugar de scripts. Una plantilla de Resource Manager es un archivo JSON que define lo que quiere implementar en Azure.
- Implementar, administrar y supervisar todos los recursos de la solución en grupo, en lugar de controlarlos individualmente.
- Vuelva a implementar la solución a lo largo del ciclo de vida de desarrollo y tenga la seguridad de que los recursos se implementan en un estado coherente.
- Defina las dependencias entre recursos de modo que se implementen en el orden correcto.
- Aplique control de acceso a todos los servicios, puesto que RBAC se integra de forma nativa en la plataforma de administración.
- Aplicar etiquetas a los recursos para organizar de manera lógica todos los recursos de la suscripción.
- Comprenda la facturación de la organización viendo los costos de un grupo de recursos que comparten la misma etiqueta.


## 4. Herramientas de supervición en Azure
- ### Azure Advisor 

Azure Advisor revalúa los recursos de Azure y trata de mejorar la confiabilidad, la seguridad y el rendimiento, lograr la excelencia operativa y reducir los costos en os recursos. Esto es posible ya que la idea es optimizar la nube ahorrandole tiempo al usuario. 

- ### Azure Service Health 

Azure Service Health le permite realizar un seguimiento de los recursos de Azure, tanto los recursos implementados específicamente como el estado general de Azure. Azure Service Health lo hace combinando tres servicios de Azure diferentes:

- **Estado de Azure** es una visión general del estado de Azure de forma global. Estado de Azure informa de las interrupciones de servicio en Azure en la página de estado de Azure . La página es una vista global del estado de todos los servicios y regiones de Azure. Es una buena referencia de los incidentes con un impacto generalizado.

- **Service Health** proporciona una vista más limitada del estado de los servicios y regiones de Azure. Se centra en los servicios y regiones de Azure que usa. Es el mejor lugar para buscar comunicaciones que afecten a los servicios relativas a interrupciones, actividades de mantenimiento planeado y otros avisos de mantenimiento, ya que tras la autenticación, Service Health conoce los servicios y recursos que usa en la actualidad. Incluso puede configurar las alertas de Service Health para que le envíen notificaciones cuando se produzcan problemas del servicio, mantenimientos planeados o cualquier otro cambio que pueda afectar a los servicios y regiones de Azure que usa.

- **Resource Health** es una vista personalizada de los recursos reales de Azure. Proporciona información sobre el estado de los recursos en la nube individuales, como una instancia de máquina virtual concreta. Mediante Azure Monitor también puede configurar alertas que le notifiquen los cambios de disponibilidad de los recursos en la nube.

- ### Azure Monitor 

![i](https://github.com/datalytics-mejorcondatos/AZ900-Azure-Fundamentals/blob/Develop/Material/Imagenes/i.png)

Azure Monitor es una plataforma para recopilar datos sobre los recursos, analizar esos datos, visualizar la información e incluso actuar en función de los resultados. Azure Monitor puede supervisar los recursos de Azure, los recursos locales e incluso los recursos de varias nubes, como las máquinas virtuales hospedadas con otro proveedor de nube.