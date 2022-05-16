import requests
import pandas as pd
import openpyxl
from datetime import date
import datetime

diaa = ['2022-05-12']
print("Today's date:", diaa)
"""dia = diaa.strftime("%d-%m-%y")"""
# ------------------------------------- Rondonia_CentroSul ----------------------------------------
for dia in diaa:
    headers = {
        "authorization": "Token dbbeb29e1436a8737114fa7e9cf1210f1a3591f5",
        "content-type": "application/json",
    }

    params = (("planned_date", diaa),)

    response = requests.get(
    "https://api.simpliroute.com/v1/routes/visits/", headers=headers, params=params
    )

    df_json = pd.read_json(response.content)
    df_json['checkin_time'] = df_json['checkin_time'].dt.tz_convert(None)
    df_json['checkout_time'] = df_json['checkout_time'].dt.tz_convert(None)
    df_json['modified'] = df_json['modified'].dt.tz_convert(None)
    df_json.sort_index(ascending=True, inplace=True)
    colunas = df_json.columns.to_list()
    colunas.sort()
    df_ordenado = df_json[colunas]
    df_json.to_excel(r"C:\Users\sacdsilva\Bureau Veritas\P&U - Solucoes Digitais - Documentos\Documentos\Clientes\ENERGISA RO\Fotos\Base de fotos\Maio_2022\SimpliRoute_Rondonia_CentroSul_"+str(dia)+".xlsx")
    print("Base de Rondonia_CentroSul exportado para excel_" + str(dia))
