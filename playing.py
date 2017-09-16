from todoist.api import TodoistAPI

f = open('token.txt', 'r')
token = f.read()
f.close()
print(token)

# api = TodoistAPI(token)
# api.sync()
# projects = api.state['projects']

# How to add a project
# project1 = api.projects.add('ProjectToAdd')
# api.commit()
#
# Add a new task
# task = api.items.add('Task Name', project1['id'])



#
# for p in projects:
#     print(p)