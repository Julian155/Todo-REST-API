from flask import Response, request, session
from Modules.Kernel.Controller.AbstractController import AbstractController
from Modules.Todo.Repository.TodoRepository import TodoRepository
from Shared.Rest.RestHttpCodes import RestHttpCodes
from Shared.Rest.Transfer.RestResponseTransfer import RestResponseTransfer
from Modules.Todo.TodoFactory import TodoFactory

class TodoListController(AbstractController):
    def getTodoListEntries(self, todoListId: str): 
        todoRepository = TodoFactory().createTodoRepository()
        
        if not todoRepository.doesTodoListExist(todoListId):
            return self.buildRespond(
                (RestResponseTransfer()
                    .setStatusCode(RestHttpCodes.RESOURCE_NOT_FOUND)
                )
            )
              
        todoEntryCollectionTransfer = todoRepository.getTodoEntryCollectionTransfer(todoListId)

        return self.buildRespond(
            (RestResponseTransfer()
                .addResponseData(todoEntryCollectionTransfer.toDict())
            )
        )
        
    def getAllTodoLists(self):
        todoListCollectionTransfer = TodoFactory().createTodoRepository().getTodoListCollectionTransfer()

        return self.buildRespond(
            (RestResponseTransfer()
                .addResponseData(todoListCollectionTransfer.toDict())
            )
        )

    def deleteTodoList(self, todoListId: str)-> Response:
        todoListEntity = TodoFactory().createTodoRepository().getTodoListById(todoListId)

        if not todoListEntity:
            return self.buildRespond(
                (RestResponseTransfer()
                    .setStatusCode(RestHttpCodes.RESOURCE_NOT_FOUND)
                )
            )
        
        TodoFactory().createTodoEntitiyManager().deleteTodoList(todoListEntity)

        return self.buildRespond(
            (RestResponseTransfer())
        )
    
    def createTodoList(self)-> Response:
        todoListData = request.json

        todoListTransfer = TodoFactory().createTodoRepository().createTodoList(todoListData)

        todoList = TodoFactory().createTodoEntitiyManager().saveTodoList(todoListTransfer)

        return self.buildRespond(
            (RestResponseTransfer()
                .addResponseData(todoList)
            )
        )

    def updateTodoList(self, todoListId: str)-> Response:
        todoListData = request.json

        todoListEntity = TodoFactory().createTodoRepository().getTodoListById(todoListId)

        TodoFactory().createTodoEntitiyManager().updateTodoList(todoListData, todoListEntity)
        
        return self.buildRespond(
            (RestResponseTransfer())
        )