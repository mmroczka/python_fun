import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pprint

scope = ['https://spreadsheets.google.com/feeds']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
client = gspread.authorize(creds)
pp = pprint.PrettyPrinter()

sheet = client.open('Legislators 2017').sheet1

result = sheet.get_all_records()

pp.pprint(result)
