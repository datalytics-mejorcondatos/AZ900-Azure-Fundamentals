from analisisrentabilidades.procesamiento import limpieza_datos_retabilidades, act_df_rentabilidades, escribir_resultados
from analisisrentabilidades.consultas import consultanit, result_rentabilidades
from analisisrentabilidades.datalake import InteractuarDataLake

Lista_fondos = "https://www.bancolombia.com/consultarFondosInversion/rest/servicio/consultarListaFondos"
url_base =  "https://www.bancolombia.com/consultarFondosInversion/rest/servicio/buscarInformacionFondo/"

# ACCOUNT_NAME = "datalakecienciadatos"
# ACCOUNT_KEY = "GjeaiEjBTpU9uCe+WcVip8kPQOyIesAxy6kvv9drKLRTgGuLVwrocehT4lowSaHi4ZT8MjWhnbth+AStdqP6/w=="

if __name__ == "__main__": 
     print("Inicio de consulta Nits")
     Nits= consultanit(Lista_fondos)
     print("Extraer rentabilidades de los fondos")
     Fond= result_rentabilidades(url_base, Nits)
     print("Limpieza de dataset final")
     DFfondos= limpieza_datos_retabilidades(Fond)
     ruta= 'Fondos.csv'
     print("Actualización de archivo histórico")
     act_df_rent = act_df_rentabilidades(ruta,DFfondos)
     print("Escritura de resultados")
     escribir_resultados(ruta, act_df_rent)

     # CONTAINER_NAME = "proyectofondos"
     # BLOB_NAME = "Fondos.csv"    

     # Interaccion con el datalake
     # Definición de la clase
     # ClaseDL = InteractuarDataLake(ACCOUNT_NAME,ACCOUNT_KEY)
     # ClaseDL.blob_client()

     # # Escritura del archivo
     # ClaseDL.escritura_container("Fondos.csv",CONTAINER_NAME, BLOB_NAME)

     # escritura desde el datalake a la mv
     # download_file_path = "Nuevo_archivo2.csv"
     # file_path = 'Fondos.csv'
     # ClaseDL.lectura_container(download_file_path,CONTAINER_NAME,file_path)