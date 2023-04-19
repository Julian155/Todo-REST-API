from flask import request, Response
from Shared.Rest.RestHttpCodes import RestHttpCodes
from Shared.Rest.Transfer.RestResponseTransfer import RestResponseTransfer
from Modules.Todo.TodoFactory import TodoFactory
from Modules.Kernel.Controller.AbstractController import AbstractController

class TodoEntryController(AbstractController):
    def addEntryToTodoList(self, todoListId: str)-> Response:
        todoEntryData = request.form

        if not TodoFactory().createTodoListRepository().doesTodoListExist(todoListId):
            return 'true', 404

        todoEntryTransfer = TodoFactory().createTodoEntryRepository().createTodoEntryTransfer(todoEntryData)

        todoEntry = TodoFactory().createTodoEntryEntityManager().saveTodoEntry(todoEntryTransfer, todoListId)

        return self.buildRespond(
            (RestResponseTransfer()
                .setStatusCode(RestHttpCodes.SUCCESS)
                .addResponseData(todoEntry)
            )
        )
    
    def updateTodoEntry(self, todoEntryId: str)-> Response:
        todoEntryData = request.form

        todoEntryEntity = TodoFactory().createTodoEntryRepository().getTodoEntryById(todoEntryId)
        todoEntryTransfer = TodoFactory().createTodoEntryRepository().createTodoEntryTransfer(todoEntryData)
        
        TodoFactory().createTodoEntryEntityManager().updateTodoEntry(todoEntryTransfer, todoEntryEntity)

        return self.buildRespond(
            (RestResponseTransfer()
                .setStatusCode(RestHttpCodes.SUCCESS)
            )
        )

    def deleteTodoEntry(self, todoEntryId: str):
        todoEntryEntity = TodoFactory().createTodoEntryRepository().getTodoEntryById(todoEntryId)

        if not todoEntryEntity:
            return '', 404
        
        TodoFactory().createTodoEntryEntityManager().deleteTodoEntry(todoEntryEntity)

        return self.buildRespond(
            (RestResponseTransfer()
                .setStatusCode(RestHttpCodes.SUCCESS)
            )
        )