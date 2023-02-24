import pandas as pd
import requests

Lista_fondos = "https://fiduciaria.grupobancolombia.com/consultarFondosInversion/rest/servicio/consultarListaFondos"
url_base =  "https://fiduciaria.grupobancolombia.com/consultarFondosInversion/rest/servicio/buscarInformacionFondo/"

#Consultar API
def consultanit(Lista_fondos):
    response = requests.get(Lista_fondos)
    fondo = response.json()
    return fondo