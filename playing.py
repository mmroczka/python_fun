from todoist.api import TodoistAPI

# How to add a project
# project1 = api.projects.add('ProjectToAdd')
# api.commit()
#
# Add a new task
# task = api.items.add('Task Name', project1['id'])

f = open('token.txt', 'r')
token = f.read().strip()
f.close()

todoist = TodoistAPI(str(token))
todoist.sync()
projects = todoist.state['projects']
labels = todoist['labels']


def get_label_from_id(id):
    ids = []
    for l in labels:
        ids.append(l['id'])
        if id == l['id']:
            return l['name']

get_label_from_id(2148311739)


tasks = todoist['items']

for t in tasks:
    if t['labels']:
        task_labels = t['labels']
        print(str(t['content']) + '\t\t', end='')
        for l in task_labels:
            print(get_label_from_id(l), end='\t')
        print()