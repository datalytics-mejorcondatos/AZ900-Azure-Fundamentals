from analisisrentabilidades.procesamiento import limpieza_datos_retabilidades, act_df_rentabilidades, escribir_resultados
from analisisrentabilidades.consultas import consultanit, result_rentabilidades
from analisisrentabilidades.datalake import InteractuarDataLake
from azure.storage.blob import BlobServiceClient

Lista_fondos = "https://www.bancolombia.com/consultarFondosInversion/rest/servicio/consultarListaFondos"
url_base =  "https://www.bancolombia.com/consultarFondosInversion/rest/servicio/buscarInformacionFondo/"

ACCOUNT_NAME = "datalakecienciadatos"
ACCOUNT_KEY = "GjeaiEjBTpU9uCe+WcVip8kPQOyIesAxy6kvv9drKLRTgGuLVwrocehT4lowSaHi4ZT8MjWhnbth+AStdqP6/w=="


if __name__ == "__main__": 
     print("Inicio de consulta Nits")
     Nits= consultanit(Lista_fondos)

     print("Extraer rentabilidades de los fondos")
     Fond= result_rentabilidades(url_base, Nits)
     
     print("Limpieza de dataset final")
     DFfondos= limpieza_datos_retabilidades(Fond)
     
     print("Lectura archivo DataLake")
     ruta= 'Fondos.csv'
     ClaseDL = InteractuarDataLake(ACCOUNT_NAME,ACCOUNT_KEY)
     CONTAINER_NAME = "proyectofondos"
     ClaseDL.blob_client()
     ClaseDL.lectura_container(ruta, CONTAINER_NAME,ruta)
     
     print("Actualización de archivo histórico")
     act_df_rent = act_df_rentabilidades(ruta,DFfondos)
    
     rutalog='log_ejecuciones.csv'
     ClaseDL.lectura_container(rutalog, CONTAINER_NAME,rutalog)
    
     print("Escritura de resultados")
     escribir_resultados(ruta, rutalog, act_df_rent)
     
     ClaseDL.escritura_container(ruta,CONTAINER_NAME,ruta)
    
     ClaseDL.escritura_container(rutalog,CONTAINER_NAME,rutalog)