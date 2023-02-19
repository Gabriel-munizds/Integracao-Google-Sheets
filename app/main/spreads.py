import gspread
from gspread_dataframe import set_with_dataframe
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd

# Definindo Parâmetros da API e da planilha a ser trabalhada
scope = ['https://spreadsheets.google.com/feeds'] # Escopo Utilizado
credentials = ServiceAccountCredentials.from_json_keyfile_name('credentials/credentials.json', scope) # Dados de Autenticação
gc = gspread.authorize(credentials) # Autenticação
id_sheet = '1Joar1DQpWKm2CSGaUYYtgmh3dS_TYJaO2OhZciIFzmo'
wks = gc.open_by_key(id_sheet) # Abre a planilha a ser utilizada
worksheet = wks.get_worksheet(1) # Seleciona a página (0,1,2...)

# Criando Objeto DataFrame para ser inserido na planilha
endereco_csv = 'database/vendas_01.01.2023_a_17.02.2023.csv'
df = pd.read_csv(endereco_csv, sep=";", encoding='latin_1')
df[' Valor Unit.'] = df[' Valor Unit.'].str.replace(",",".").astype(float)
df[' Valor Total'] = df[' Valor Total'].str.replace(",", ".").astype(float)
print(df.head())
print(df.info())

# inserindo dados
set_with_dataframe(worksheet,df)
print('Dados carregados com sucesso!')



