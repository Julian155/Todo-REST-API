from flask import request, Response
from Shared.Rest.RestHttpCodes import RestHttpCodes
from Shared.Rest.Transfer.RestResponseTransfer import RestResponseTransfer
from Modules.Todo.TodoFactory import TodoFactory
from Modules.Kernel.Controller.AbstractController import AbstractController

class TodoEntryController(AbstractController):
    def addEntryToTodoList(self, todoListId: str)-> Response:
        todoEntryData = request.json

        if not TodoFactory().createTodoRepository().doesTodoListExist(todoListId):
            return self.buildRespond(
                (RestResponseTransfer()
                    .setStatusCode(RestHttpCodes.RESOURCE_NOT_FOUND)
                )
            )

        todoEntryTransfer = TodoFactory().createTodoRepository().createTodoEntryTransfer(todoEntryData)

        todoEntry = TodoFactory().createTodoEntitiyManager().saveTodoEntry(todoEntryTransfer, todoListId)

        return self.buildRespond(
            (RestResponseTransfer()
                .addResponseData(todoEntry)
            )
        )
    
    def updateTodoEntry(self, todoEntryId: str)-> Response:
        todoEntryData = request.json

        todoEntryEntity = TodoFactory().createTodoRepository().getTodoEntryById(todoEntryId)
        
        if not todoEntryEntity:
            return self.buildRespond(
                (RestResponseTransfer()
                    .setStatusCode(RestHttpCodes.RESOURCE_NOT_FOUND)
                )
            )
            
        todoEntryTransfer = TodoFactory().createTodoRepository().createTodoEntryTransfer(todoEntryData)
        
        TodoFactory().createTodoEntitiyManager().updateTodoEntry(todoEntryTransfer, todoEntryEntity)

        return self.buildRespond(
            (RestResponseTransfer())
        )

    def deleteTodoEntry(self, todoEntryId: str):
        todoEntryEntity = TodoFactory().createTodoRepository().getTodoEntryById(todoEntryId)

        if not todoEntryEntity:
            return self.buildRespond(
                (RestResponseTransfer()
                    .setStatusCode(RestHttpCodes.RESOURCE_NOT_FOUND)
                )
            )
        
        TodoFactory().createTodoEntitiyManager().deleteTodoEntry(todoEntryEntity)

        return self.buildRespond(
            (RestResponseTransfer())
        )