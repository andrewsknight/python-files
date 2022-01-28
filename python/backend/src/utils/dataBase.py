import os


def createTable(name):
    file = 'database/' + name
    if not os.path.exists(file):
        os.mknod(file)


usersKeys = ['name', 'lastname', 'age']
attendsKeys = ['name', 'lastname', 'email', 'phone', 'attend']


def saveEntity(entityName, entitysKeys, entity):
    createTable(entityName)
    entityStr = ''
    for key in entitysKeys:
        entityStr += entity[key] + '#'
    entityStr = entityStr[:-1]
    entityDataBase = open('database/'+entityName, 'a+')
    entityDataBase.write('\n')
    entityDataBase.write(entityStr)


def saveAttend(attend):
    saveEntity('attends', attendsKeys, attend)


def saveUser(person):
    saveEntity('users', usersKeys, person)
