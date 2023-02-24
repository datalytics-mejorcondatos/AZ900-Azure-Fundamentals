import pandas as pd
import requests
import io
from urllib.parse import urlencode

import sys
# sys.path.append('c:\\Users\\nataly.ramirez\\AZ900-Azure-Fundamentals\\')
from funciones import fondofinal

Lista_fondos = "https://fiduciaria.grupobancolombia.com/consultarFondosInversion/rest/servicio/consultarListaFondos"
url_base =  "https://fiduciaria.grupobancolombia.com/consultarFondosInversion/rest/servicio/buscarInformacionFondo/"

DFfondofinal= fondofinal(Lista_fondos, url_base)
DFfondofinal
