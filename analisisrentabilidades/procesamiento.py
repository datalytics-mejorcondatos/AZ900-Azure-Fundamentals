import pandas as pd
import os
import csv
import datetime

def limpieza_datos_retabilidades(resultados_fondos):
    """
    Esta función crea un dataframe con la información de los fondos de inversión como salida. Extrae los diccionarios de rentabilidades por días y años para luego posicionarlos en columnas nuevas.
    
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

def act_df_rentabilidades(ruta_lectura,df_renta):

    df_renta = df_renta.query("~fechaCierre.isna()").copy()
    df_renta["fechaCierre"] = pd.to_datetime(df_renta["fechaCierre"].astype(int), format = "%Y%m%d")
    df_renta["fechaCierre"] = df_renta["fechaCierre"].dt.strftime("%Y-%m-%d")

    if os.path.exists(ruta_lectura):

        version1_df = pd.read_csv(ruta_lectura)
        print(version1_df.shape[0])
        full_df_renta = pd.concat([version1_df,df_renta],axis=0)
        
        full_df_renta.drop_duplicates(subset=["nit","fechaCierre"], inplace = True)
        print(full_df_renta.shape[0])
        return full_df_renta
    else:        
        return df_renta
    
def escribir_resultados(ruta, rutalog, act_df_rent):
    fecha_actual = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')  
    with open(ruta, "r") as archivo:
        lineas_antes = len(list(csv.reader(archivo)))
    act_df_rent.to_csv(ruta, index=False)
    with open(ruta, "r") as archivo:
        lineas_despues = len(list(csv.reader(archivo)))
    lineas_nuevas = lineas_despues - lineas_antes
    with open(rutalog, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([fecha_actual, lineas_nuevas])