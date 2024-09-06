import os
import json
from dotenv import load_dotenv
from google.oauth2 import service_account
from googleapiclient.discovery import build
import calendar
from datetime import datetime

load_dotenv() #loading .env file

SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
SPREADSHEET_ID  = os.getenv("SPREADSHEET_ID")
GOOGLE_CREDINTIALS = json.loads(os.getenv("GOOGLE_CREDINTIALS"))

now = datetime.now()
year = now.year
month = now.month
day = now.day

days_in_month = calendar.monthrange(year, month)[1]

def get_service():
    #load credentials from a dictionary
    creds = service_account.Credentials.from_service_account_info(
        GOOGLE_CREDINTIALS, scopes=SCOPES
    )
    service = build('sheets', 'v4', credentials=creds)
    return service.spreadsheets()


# Read Operation
def read_data():
    service = get_service()
    range_ = f'main!A2:G{days_in_month+1}'
    print(day)
    result = service.values().get(spreadsheetId=SPREADSHEET_ID, range=range_).execute()
    return result.get('values', [])


def add_data(data):
    service  = get_service()
    range_ = f'main!A{day+1}:G{day+1}'
    value_input_option = 'RAW'
    insert_data_option = 'INSERT_ROWS'

    data = [int(x) for x in data]
    
    body = {
        'values': [
                [day] + data
            ]
    }

    result = service.values().append(
        spreadsheetId=SPREADSHEET_ID,
        range=range_,
        valueInputOption=value_input_option,
        insertDataOption=insert_data_option,
        body=body
    ).execute()

    print(result)


