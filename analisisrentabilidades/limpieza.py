import pandas as pd
import numpy as np

def limpieza_datos_retabilidades(resultados_fondos):

    """
    
    que hace funciones

    Parameters:

        resultados_fondos: pandas.DataFrame: Los resultados de los fondos de inversion de bancolombia.
    
    Returns:

        pandas.DataFrame: DataFrame limpio con la información de los resultados de los fondos de inversion.

    
    """

    Totaldf= pd.DataFrame()

    for nit in resultados_fondos:
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
    
    return rentabilidades_fondos_clean