import requests

#Consultar API
def consultanit(Lista_fondos):
    response = requests.get(Lista_fondos)
    fondo = response.json()

    codigo = [fondo[i]["nit"] for i in range(len(fondo))]
    print(len(codigo))
    codigo = list(set(codigo))
    print(len(codigo))

    return codigo

def result_rentabilidades(url_base, lista_nits):
    
    consultas= [url_base + nit for nit in lista_nits]
    infofondos=[requests.get(url_renta).json() for url_renta in consultas]
    return infofondos