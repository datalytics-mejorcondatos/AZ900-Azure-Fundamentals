import pandas as pd
import requests
from urllib.parse import urlencode
import sys
sys.path.append('c:\\Users\\nataly.ramirez\\AZ900-Azure-Fundamentals\\')
from analisisrentabilidades.consultanit import consultanit

Lista_fondos = "https://fiduciaria.grupobancolombia.com/consultarFondosInversion/rest/servicio/consultarListaFondos"
url_base =  "https://fiduciaria.grupobancolombia.com/consultarFondosInversion/rest/servicio/buscarInformacionFondo/"


def result_rentabilidades(url_base):
    codigo = [consultanit(Lista_fondos)[i]["nit"] for i in range(len(consultanit(Lista_fondos)))]
    consultas= [url_base + codigo[i] for i in range(len(codigo))]
    infofondos=[requests.get(consultas[i]).json() for i in range(len(consultas))]
    return infofondos