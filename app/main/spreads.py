import gspread
from oauth2client.service_account import ServiceAccountCredentials


# Definindo Parâmetros da API e da planilha a ser trabalhada
scope = ['https://spreadsheets.google.com/feeds'] # Escopo Utilizado
credentials = ServiceAccountCredentials.from_json_keyfile_name('credentials/credentials.json', scope) # Dados de Autenticação
gc = gspread.authorize(credentials) # Autenticação
wks = gc.open_by_key('1yp2UhmO1HmSE-LjBFrLLxrT_33A_Q2gEMcs1B-rtrAk') # Abre a planilha a ser utilizada
worksheet = wks.get_worksheet(0)

# inserindo dados
worksheet.update_acell('A1', 'FUNCIONOU')


