from todoist.api import TodoistAPI
token = '1abc92a3b1964c8188b305f84e6e0240ff9b702b'
api = TodoistAPI(token)
api.sync()
print(api.state['projects'])