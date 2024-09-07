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
current_day = now.day

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
    result = service.values().get(spreadsheetId=SPREADSHEET_ID, range=range_).execute()
    return result.get('values', [])


def add_data_meal(data, day=None):
    service  = get_service()

    if day is None:
        day = current_day

    range_ = f'main!A{day+1}:G{day+1}'

    result = service.values().get(spreadsheetId=SPREADSHEET_ID, range=range_).execute()


    if 'values' in result and result['values']:
        return {"status": "error", "message": "Data exists. Proceed to 'update/' if needed"}


    data = [int(x) for x in data]
    
    body = {
        'values': [
                [day] + data
            ]
    }
    value_input_option = 'RAW'
    insert_data_option = 'INSERT_ROWS'
    result = service.values().append(
        spreadsheetId=SPREADSHEET_ID,
        range=range_,
        valueInputOption=value_input_option,
        insertDataOption=insert_data_option,
        body=body
    ).execute()

    return {"status": "success", "message": "Data appended successfully."}

def update_data_meal(data, day, user):
    service = get_service()
    headings = f'main!A1:G1'

    result = service.values().get(spreadsheetId=SPREADSHEET_ID, range=headings).execute()
    users = [x.lower() for x in result['values'][0]]

    data = [int(x) for x in data]

    body = {
        'values': [
                data
            ]
    }
    
    if user not in users:
        return {"status": "failed", "message": "User not found"}

    index = users.index(user) + 65
    range_ = f'main!{chr(index)}{day+1}:{chr(index)}{day+1}'

    result = service.values().get(spreadsheetId=SPREADSHEET_ID, range=range_).execute()

    if 'values' not in result or not result['values']:
        return {"status": "failed", "message": "No data found"}

    result = service.values().update(spreadsheetId=SPREADSHEET_ID, range=range_, valueInputOption='RAW', body=body).execute()  

    return {"status": "success", "message": "Updated Successfully"}


def delete_row(day):
    service = get_service()
    range_ = f"A{day+1}:G{day+1}"

    result = service.values().get(spreadsheetId=SPREADSHEET_ID, range=range_).execute()

    if 'values' not in result or not result['values']:
        return {"status": "failed", "message": "No data found"}

    result = service.values().clear(spreadsheetId=SPREADSHEET_ID, range=range_).execute()
    return {"status": "success", "message": "Deleted Successfully"}
    

def add_given(data, day=None):
    service = get_service()

    if day is None:
        day = current_day

    range_ = f'given!A{day+1}:G{day+1}'

    result = service.values().get(spreadsheetId = SPREADSHEET_ID, range = range_).execute()

    if 'values' in result and result['values']:
        return {"status": "failed", "message": "Data already exists"}

    data = [int(x) for x in data]

    body = {
        'values': [
                [day] + data
            ]
    }

    value_input_option = 'RAW'
    insert_data_option = 'INSERT_ROWS'
    result = service.values().append(
        spreadsheetId = SPREADSHEET_ID,
        range = range_,
        valueInputOption = value_input_option,
        insertDataOption = insert_data_option,
        body = body
    ).execute()

    return {"status": "success", "message": "Data appended successfully."}

    
