import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pprint

# from todoist.api import TodoistAPI

# How to add a project
# project1 = api.projects.add('ProjectToAdd')
# api.commit()
#
# Add a new task
# task = api.items.add('Task Name', project1['id'])

# f = open('token.txt', 'r')
# token = f.read().strip()
# f.close()
#
# todoist = TodoistAPI(str(token))
# todoist.sync()
# projects = todoist.state['projects']
# labels = todoist['labels']
#
#
# def get_label_from_id(id):
#     ids = []
#     for l in labels:
#         ids.append(l['id'])
#         if id == l['id']:
#             return l['name']
#
# get_label_from_id(2148311739)
#
#
# tasks = todoist['items']
#
# for t in tasks:
#     if t['labels']:
#         task_labels = t['labels']
#         print(str(t['content']) + '\t\t', end='')
#         for l in task_labels:
#             print(get_label_from_id(l), end='\t')
#         print()


scope = ['https://spreadsheets.google.com/feeds']
creds = ServiceAccountCredentials.from_json_keyfile_name('new_client_secret.json', scope)
client = gspread.authorize(creds)
pp = pprint.PrettyPrinter()

def next_available_row(worksheet):
    str_list = list(filter(None, worksheet.col_values(1)))  # fastest
    return str(len(str_list)+1)

i_am_ironman = client.open('I Am Ironman')
practice = i_am_ironman.worksheet('Practice')
next_row = int(next_available_row(practice))
values = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
practice.insert_row(values, next_row)
