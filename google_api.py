
from google.oauth2 import service_account
from googleapiclient.discovery import build
import datetime
import json

# Adicionar evento ao Google Calendar
def adicionar_evento_calendar(nome_evento):
    try:
        with open("config.json") as f:
            config = json.load(f)

        SCOPES = ['https://www.googleapis.com/auth/calendar']
        creds = service_account.Credentials.from_service_account_file(
            'utils/credentials_calendar.json', scopes=SCOPES)

        service = build('calendar', 'v3', credentials=creds)

        hoje = datetime.date.today()
        evento = {
            'summary': nome_evento,
            'start': {'date': str(hoje), 'timeZone': 'America/Sao_Paulo'},
            'end': {'date': str(hoje), 'timeZone': 'America/Sao_Paulo'}
        }

        service.events().insert(calendarId=config['calendar_id'], body=evento).execute()
        print("✅ Evento adicionado ao Google Calendar com sucesso.")
    except Exception as e:
        print("❌ Erro ao adicionar evento ao Calendar:", e)

# Salvar time sugerido no Google Sheets
def salvar_fantasy_sheet(pilotos_df, equipes_df):
    try:
        with open("config.json") as f:
            config = json.load(f)

        SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
        creds = service_account.Credentials.from_service_account_file(
            'utils/credentials_calendar.json', scopes=SCOPES)

        service = build('sheets', 'v4', credentials=creds)
        sheet = service.spreadsheets()

        data = [[
            datetime.date.today().isoformat(),
            ", ".join(pilotos_df['Piloto']),
            ", ".join(equipes_df['Equipe']),
            str(pilotos_df['Nota'].sum() + equipes_df['Nota'].sum())
        ]]

        body = {'values': data}
        sheet.values().append(
            spreadsheetId=config['spreadsheet_id'],
            range='A1',
            valueInputOption='USER_ENTERED',
            insertDataOption='INSERT_ROWS',
            body=body
        ).execute()
        print("✅ Time salvo no Google Sheets com sucesso.")
    except Exception as e:
        print("❌ Erro ao salvar no Google Sheets:", e)
