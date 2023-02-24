import pandas as pd
import numpy as np
import requests
from urllib.parse import urlencode

lista_fondos = "https://fiduciaria.grupobancolombia.com/consultarFondosInversion/rest/servicio/consultarListaFondos"
url_base =  "https://fiduciaria.grupobancolombia.com/consultarFondosInversion/rest/servicio/buscarInformacionFondo/"


#Función grande

def fondofinal(Lista_fondos, url):
    response = requests.get(Lista_fondos)
    fondo = response.json()
    codigo = [fondo[i]["nit"] for i in range(len(fondo))]
    print(codigo)
    consultas= [url_base + codigo[i] for i in range(len(codigo))]
    consultas
    infofondos=[requests.get(consultas[i]).json() for i in range(len(consultas))]
    Totaldf= pd.DataFrame()
    for nit in infofondos:
        df = pd.DataFrame(nit).reset_index(drop=True)
        Totaldf = pd.concat([Totaldf,df],axis=0)

    Totaldf.reset_index(drop=True, inplace=True)

    anual = Totaldf["rentabilidad"].apply(pd.Series).iloc[:,:4].copy()
    anual.dropna(inplace=True)
    anual.reset_index(inplace=True,drop=True)

    diarios = Totaldf["rentabilidad"].apply(pd.Series).iloc[:,4:].reset_index(drop=True).copy()
    diarios.dropna(inplace=True)
    diarios.reset_index(inplace=True,drop=True)

    rentabilidades = pd.concat([anual,diarios],axis=1)
    # rentabilidades

    # limpiar dataset original
    Totaldf.drop(["rentabilidad"],axis=1, inplace=True)

    Totaldf.drop_duplicates(inplace=True)
    Totaldf.reset_index(inplace=True, drop=True)
    Totaldf

    #unificar datasets
    rentabilidades_fondos_clean = pd.concat([Totaldf,rentabilidades],axis=1)
    ruta= 'Archivofondos'
    Archivo= rentabilidades_fondos_clean.to_csv(ruta, index=False)
    return Archivo