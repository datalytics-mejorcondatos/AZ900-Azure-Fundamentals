from analisisrentabilidades.limpieza import limpieza_datos_retabilidades
from analisisrentabilidades.consultanit import consultanit
from analisisrentabilidades.infofondos import result_rentabilidades

Lista_fondos = "https://fiduciaria.grupobancolombia.com/consultarFondosInversion/rest/servicio/consultarListaFondos"
url_base =  "https://fiduciaria.grupobancolombia.com/consultarFondosInversion/rest/servicio/buscarInformacionFondo/"



if __name__ == "__main__": 
     print("Inicio de consulta Nits")
     Nits= consultanit(Lista_fondos)
     print("Extraer rentabilidades de los fondos")
     Fond= result_rentabilidades(url_base)
     print("Limpieza de dataset final")
     DFfondos= limpieza_datos_retabilidades(Fond)
     print("Escritura de resultados")
     ruta= 'Fondos.csv'
     Archivo= DFfondos.to_csv(ruta, index=False)