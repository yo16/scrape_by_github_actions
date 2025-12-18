"""
Google Spread Sheetsにデータを書き込む
"""
from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build

SCOPES = [
    "https://www.googleapis.com/auth/spreadsheets",
]

SERVICE_ACCOUNT_FILE = "credentials/service_account.json"

SPREADSHEET_ID = "1TBpDvJOayrXaqNz4BOi2cB2zVMMMkgUoIKYqJCLduq0"
SHEET_NAME = "ScrapedData"


def write_to_google_sheets(article_list):
    creds = Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE,
        scopes=SCOPES
    )
    
    service = build("sheets", "v4", credentials=creds)

    sheet = service.spreadsheets()

    # データを追加（appendメソッドは自動的に最終行の後に追加）
    if article_list:  # データが空でないことを確認
        sheet.values().append(
            spreadsheetId=SPREADSHEET_ID,
            range=SHEET_NAME,
            valueInputOption="USER_ENTERED",
            body={
                "values": article_list
            }
        ).execute()

