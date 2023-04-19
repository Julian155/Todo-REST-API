import json
from flask import session
from Modules.Todo.Repository.Persistence.TodoEntryEntity import TodoEntryEntity
from Modules.Todo.Repository.Persistence.TodoListEntity import TodoListEntity

class SessionBuilder():
    def initSessionStructure(self)-> None:
        with open('SessionStructure.json') as sessionStructureJsonFile:
            session.update(json.load(sessionStructureJsonFile))
            session.permanent = True

        with open('DemoData.json') as demoDataJsonFile:
            demoData = json.load(demoDataJsonFile)
            
            for todoListData in demoData['todoLists']:
                todoListEntity = TodoListEntity().fromDict(todoListData)
                todoListEntity.save()

            for todoEntryData in demoData['todoEntries']:
                todoEntryEntity = TodoEntryEntity().fromDict(todoEntryData)
                todoEntryEntity.save()