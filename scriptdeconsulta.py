from analisisrentabilidades.procesamiento import limpieza_datos_retabilidades, act_df_rentabilidades, escribir_resultados
from analisisrentabilidades.consultas import consultanit, result_rentabilidades

Lista_fondos = "https://www.bancolombia.com/consultarFondosInversion/rest/servicio/consultarListaFondos"
url_base =  "https://www.bancolombia.com/consultarFondosInversion/rest/servicio/buscarInformacionFondo/"

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