# AZ900-Azure-Fundamentals

### Este repositorio está creado para ser una guía al momento de iniciar el estudio para obtener la certificación de [AZ900-Azure-Fundamentals](https://learn.microsoft.com/en-us/certifications/exams/az-900/)

Esta certificación está enfocada en el dominio de los conceptos básicos de la computación en la nube de Azure.

## Contenido

- [Material](./Material)
  1. [Conceptos](./Material/1.%20Descripción%20de%20los%20conceptos%20de%20nube)
        - [Descripción de los conceptos básicos en la nube](./Material/1.%20Descripci%C3%B3n%20de%20los%20conceptos%20de%20nube/Conceptos_basicos.md)
  2. [Arquitectura y servicios](./Material/2.%20Descripci%C3%B3n%20de%20la%20arquitectura%20y%20los%20servicios%20de%20Azure)
        - [Descripción de la Arquitectura y servicios de Azure](./Material/2.%20Descripci%C3%B3n%20de%20la%20arquitectura%20y%20los%20servicios%20de%20Azure/Arquitectura_y_servicios.md)
  3. [Administración y Gobernanza](./Material/3.%20Descripci%C3%B3n%20de%20la%20administraci%C3%B3n%20y%20la%20gobernanza%20de%20Azure/)
        - [Descripción y conceptos de la Administración y Gobernanza de Azure](./Material/3.%20Descripci%C3%B3n%20de%20la%20administraci%C3%B3n%20y%20la%20gobernanza%20de%20Azure/Administraci%C3%B3n_y_gobernanza.md)
  - [Descripción de otros recursos](./Material/Descripci%C3%B3n%20otros%20recursos/README.md)
  - [Exámenes guía](./Material/Ex%C3%A1menes%20gu%C3%ADa/)
- [Funciones del análisis de rentabilidades](./analisisrentabilidades/) Esta carpeta contiene las funciones empleadas en el proyecto.


A continuación encontrará un conjunto de recursos distribuidos en carpetas en las cuales hay material especificado por tema para el estudio de la certificación. Además, podrá usar material dispuesto para la preparación del examen.

Encontrará material de las siguientes temáticas que corresponden a los módulos que son evaluados al momento de realizar el examen. El porcentaje al lado de cada módulo corresponde a la ponderación para el total del examen. 

- Descripción de los conceptos de la nube (25-30 %)
- Descripción de la arquitectura y los servicios de Azure (35-40 %)
- Descripción de la administración y la gobernanza de Azure (30-35 %)
    
Además, encontrará examenes resueltos que ayudarán al fortalecimiento de los conceptos para la presentación del examen. 

En este repositorio también se realiza un proyecto con el fin de fortalecer los conceptos de máquinas virtuales en el cual se extrae información de fondos de inversión de Bancolombia por medio de una API, donde através de una serie de módulos de python, estos fondos se actualizan de forma diaria.

En la carpeta llamada **analisisrentabilidades** se encuentran dos módulos que contienen las funciones creadas para la extracción de la información de los fondos.  

- Consultas: Este módulo contiene una función llamada *consultanit* y lo que hace es consultar los NITs que hay en la página de [Bancolombia](https://www.bancolombia.com/consultarFondosInversion/rest/servicio/consultarListaFondos) y los extrae en una lista.

      Por otro lado se tiene una función llamada *result_rentabilidades* donde toma la lista que se creó en la anterior función para pegar cada valor (NIT) en una URL y así poder consultar la información de cada uno de los fondos. 

- Procesamiento: Este módulo contiene la función *limpieza_datos_retabilidades*. Esta función crea un dataframe con la información de los fondos de inversión como salida. Extrae los diccionarios de rentabilidades por días y años para luego posicionarlos en columnas nuevas.

      También encontramos la función  *act_df_rentabilidades* donde primero, se eliminan los registros cuya fecha de cierre esté vacía y ajusta el formato de esta columna a un formato de fecha. Además concatena al dataframe que ya existe, las filas que se actualizan directamente en la página de Bancolombia a medida que se va ejecutando el script principal.

      Por último tenemos la función *escribir_resultados* que genera un archivo donde se registra la fecha de ejecución del script y las lineas que fueron agregadas.

Los archivos que encuentran en la vista principal son el script que ejecuta el proyecto y los requerimientos que este módulo de python necesita para ser ejecutado.

El módulo *scriptdeconsulta* organiza las funciones mencionadas anteriormente con los pasos necesarios para obtener un dataframe que contenga la información de los fondos de inversión de Bancolombia. 

Y los archivos que encuentra en la vista principal son el script que ejecuta el proyecto y los requerimientos que este módulo de python necesita para ser ejecutado.

Herramientas con las que se construyó el proyecto: 

- Python: versión 3.10.6
- Git/GitHub
- Azure Virtual Machines