import gspread
from gspread_dataframe import set_with_dataframe
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd

# Definindo Parâmetros da API e da planilha a ser trabalhada
scope = ['https://spreadsheets.google.com/feeds'] # Escopo Utilizado
credentials = ServiceAccountCredentials.from_json_keyfile_name('app\main\credentials\credentials.json', scope) # Dados de Autenticação
gc = gspread.authorize(credentials) # Autenticação
id_sheet = '1Joar1DQpWKm2CSGaUYYtgmh3dS_TYJaO2OhZciIFzmo'
wks = gc.open_by_key(id_sheet) # Abre a planilha a ser utilizada
worksheet = wks.get_worksheet(0) # Seleciona a página (0,1,2...)

# Criando Objeto DataFrame para ser inserido na planilha
endereco_csv = 'app\main\database\docs_relatorio_vendas84663426.csv'
df = pd.read_csv(endereco_csv, sep=";", encoding='latin_1')
df[' Valor Unit.'] = df[' Valor Unit.'].str.replace(",",".").astype(float)
df[' Valor Total'] = df[' Valor Total'].str.replace(",", ".").astype(float)
print(df.head())
print(df.info())

# identificando última linha preenchida
gs = worksheet.get_all_values()
df_gs = pd.DataFrame(gs)
next_row = len(gs) + 1

valor = df.tail(1)['Data'].iloc[0]

# inserindo dados
set_with_dataframe(worksheet, df, row = next_row, include_column_header=False)
print('Dados carregados com sucesso!')
print(f'Atualizado até {valor}')



