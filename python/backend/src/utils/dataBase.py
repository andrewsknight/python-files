import os

def createTable(name):
    file = 'database/' + name
    if not os.path.exists(file):
        os.mknod(file)

usersKeys = ['name', 'lastname', 'age']

def save(person):
    createTable('user')
    userStr = ''
    for key in usersKeys:
        userStr += person[key] + '#'
    userStr = userStr[:-1]
    userDataBase = open('database/user','a+')
    userDataBase.write('\n')
    userDataBase.write(userStr)
