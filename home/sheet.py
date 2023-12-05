from __future__ import print_function
from __future__ import print_function
from googleapiclient.discovery import build
from google.oauth2 import service_account

# Spreadsheet id
SPREADSHEET_ID = "1GkUjEGQuVWrUpXqiEqh18a6Svo1oBNUT6ilGM31mUlw"

# Sheet Name and Range to Read
SHEET_NAME = "Sheet1"
READ_RANGE = f"{SHEET_NAME}!A1:XFD1048576"  # A1 to the last column (XFD) and the last row (1048576)
WRITE_RANGE = f"{SHEET_NAME}!A1:XFD1048576"

# The boundary of script
SCOPES = [
    'https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/drive'
]


# Configuration for python to sheet link
credentials = service_account.Credentials.from_service_account_file(
    'credentials.json', scopes=SCOPES)
spreadsheet_service = build('sheets', 'v4', credentials=credentials)
drive_service = build('drive', 'v3', credentials=credentials)


# Module to read from specific range from google sheet
# def read_range():
#     range_name = READ_RANGE
#     spreadsheet_id = SPREADSHEET_ID
#     result = spreadsheet_service.spreadsheets().values().get(
#         spreadsheetId=spreadsheet_id, range=range_name).execute()
#     rows = result.get('values', [])
#     print('\t{0} cells retrieved.'.format(len(rows)))
#     print('{0} rows retrieved.'.format(rows))
#     return rows

# Module to write to the specified range of columns in google sheet
def get_last_row_number():
    result = spreadsheet_service.spreadsheets().values().get(
        spreadsheetId=SPREADSHEET_ID, range=READ_RANGE).execute()
    values = result.get('values', [])
    return len(values)


def write_new_row(data):
    last_row = get_last_row_number() + 1
    range_to_write = f"{SHEET_NAME}!A{last_row}:J{last_row}"

    value_input_option = 'USER_ENTERED'
    body = {
        'values': [data]  # Replace [data] with your new row of data
    }

    result = spreadsheet_service.spreadsheets().values().update(
        spreadsheetId=SPREADSHEET_ID, range=range_to_write,
        valueInputOption=value_input_option, body=body).execute()

    print("Data written to sheet!")

