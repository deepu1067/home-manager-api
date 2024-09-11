import os
import json
from dotenv import load_dotenv
from google.oauth2 import service_account
from googleapiclient.discovery import build
import calendar
from datetime import datetime

load_dotenv()  # loading .env file

SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]
SPREADSHEET_ID = os.getenv("SPREADSHEET_ID")
GOOGLE_CREDINTIALS = json.loads(os.getenv("GOOGLE_CREDINTIALS"))

now = datetime.now()
year = now.year
month = now.month
current_day = now.day

days_in_month = calendar.monthrange(year, month)[1]


def get_service():
    # load credentials from a dictionary
    creds = service_account.Credentials.from_service_account_info(
        GOOGLE_CREDINTIALS, scopes=SCOPES
    )
    service = build("sheets", "v4", credentials=creds)
    return service.spreadsheets()


def _get_user(user):
    # getting the index of the user
    service = get_service()
    headings = f"main!B1:G1"

    result = (
        service.values().get(spreadsheetId=SPREADSHEET_ID, range=headings).execute()
    )
    users = [x.lower() for x in result["values"][0]]

    if user in users:
        return users.index(user) + 1
    return -1


def isSheet(sheet):
    service = get_service()

    result = service.get(spreadsheetId=SPREADSHEET_ID).execute()

    sheets_response = result.get("sheets", [])
    sheets = [sheet["properties"]["title"] for sheet in sheets_response]

    return True if sheet in sheets else False


def read_data():
    # reading the 'main' sheet
    service = get_service()
    range_ = f"main!A2:G{days_in_month+1}"
    result = service.values().get(spreadsheetId=SPREADSHEET_ID, range=range_).execute()
    return result.get("values", [])


def read_data_given():
    # reading the 'given' sheet
    service = get_service()
    range_ = f"given!A2:G{days_in_month+1}"
    result = service.values().get(spreadsheetId=SPREADSHEET_ID, range=range_).execute()
    return result.get("values", [])


def add(data, user, sheet, day=None):
    # inserting data to the sheet
    service = get_service()

    if day is None:
        day = current_day

    if _get_user(user) == -1:
        return {"status": "failed", "message": "User not found"}


    if not isSheet(sheet):
        return {"status": "failed", "message": "Invalid sheet name"}
    

    index = _get_user(user) + 65
    range_ = f"{sheet}!{chr(index)}{day+1}:{chr(index)}{day+1}"

    result = service.values().get(spreadsheetId=SPREADSHEET_ID, range=range_).execute()

    if "values" in result and result["values"]:
        return {
            "status": "error",
            "message": "Data exists",
        }
    data = [int(x) for x in data]

    body = {"values": [data]}
    result = (
        service.values()
        .update(
            spreadsheetId=SPREADSHEET_ID,
            range=range_,
            valueInputOption="RAW",
            body=body,
        )
        .execute()
    )

    return {"status": "success", "message": "Data appended successfully."}


def update_data(data, day, user, sheet):
    # updaing sheet data
    service = get_service()

    data = [int(x) for x in data]

    body = {"values": [data]}

    if _get_user(user) == -1:
        return {"status": "failed", "message": "User not found"}

    if not isSheet(sheet):
        return {"status": "failed", "message": "Invalid sheet name"}
    
    index = _get_user(user) + 65
    range_ = f"{sheet}!{chr(index)}{day+1}:{chr(index)}{day+1}"
    print(range_)

    result = service.values().get(spreadsheetId=SPREADSHEET_ID, range=range_).execute()

    if "values" not in result or not result["values"]:
        return {"status": "failed", "message": "No data found"}

    result = (
        service.values()
        .update(
            spreadsheetId=SPREADSHEET_ID,
            range=range_,
            valueInputOption="RAW",
            body=body,
        )
        .execute()
    )

    return {"status": "success", "message": "Updated Successfully"}


def delete_row(day, sheet):
    # deleting row for a given day and name of the sheet
    service = get_service()

    if not isSheet(sheet):
        return {"status": "failed", "message": "Invalid sheet name"}
    

    range_ = f"{sheet}!A{day+1}:G{day+1}"
    print(range_)
    result = service.values().get(spreadsheetId=SPREADSHEET_ID, range=range_).execute()

    if "values" not in result or not result["values"]:
        return {"status": "failed", "message": "No data found"}

    result = (
        service.values().clear(spreadsheetId=SPREADSHEET_ID, range=range_).execute()
    )

    return {"status": "success", "message": "Deleted Successfully"}


def get_total(user=None):
    service = get_service()

    users = get_user()[0]
    print(users)
    if user is None:
        range_ = "main!B34:G34"
        meal = service.values().get(spreadsheetId=SPREADSHEET_ID, range=range_).execute()
        total_meal = sum(sum(int(x) for x in row) for row in meal.get("values", []))

        range_ = "given!B34:G34"
        given = service.values().get(spreadsheetId=SPREADSHEET_ID, range=range_).execute()
        total_given = sum(sum(int(x) for x in row) for row in given.get("values", []))

        result = {
            "users": users,
            "meal": meal.get("values", []),
            "given": given.get("values", []),
            "totalmeal": total_meal,
            "totalgiven": total_given,
        }

        return {"status": "success", "message": result}


    user = user.lower()

    if _get_user(user) == -1:
        return {"status": "failed", "message": "User not found"}

    index = _get_user(user) + 65

    range_ = f"main!{chr(index)}34"
    meal = service.values().get(spreadsheetId=SPREADSHEET_ID, range=range_).execute()
    

    range_ = f"given!{chr(index)}34"
    given = service.values().get(spreadsheetId=SPREADSHEET_ID, range=range_).execute()
    
    result = {
        "meal": meal.get("values", []),
        "given": given.get("values", []),
    }

    return {"status": "success", "message": result}


def get_user():
    service = get_service()

    range_ = "main!B1:G1"

    result = service.values().get(spreadsheetId=SPREADSHEET_ID, range=range_).execute()
    return result.get("values", [])


def get_list(user, sheet):
    service = get_service()

    if _get_user(user) == -1:
        return {"status": "failed", "message": "User not found"}

    if not isSheet(sheet):
        return {"status": "failed", "message": "Invalid sheet name"}

    index = _get_user(user) + 65
    range_ = f"{sheet}!{chr(index)}2:{chr(index)}{current_day+1}"

    # print(isSheet(sheet))

    result = service.values().get(spreadsheetId=SPREADSHEET_ID, range=range_).execute()

    return result.get("values", [])
